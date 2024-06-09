import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import pandas as pd
from .forms import *
import numpy as np
from django.core.files import File

# Create your views here.
def DRP_app(request):
    return render(request, 'DRP/generale.html')

def generale(request):
    return render(request, 'DRP/generale.html')

#-------------------fonction pour calculer la prévision total de entrepot central
def caclul_prevision_total():
    depots = Depot.objects.all()
    prevision_np_total = np.zeros(52)
    # get the xlsx files of previons of all depots and convert them to dataframes and then to np arrays
    for depot in depots:
        prevision_df = pd.read_excel(depot.prevision_depot)
        prevision_df.columns = ['semaine', 'prevision']
        prevision_np = prevision_df.values
        prevision_np = prevision_np[:,1]
        prevision_np_total = prevision_np_total + prevision_np
    # convert the np array of prevision total to a dataframe
    df_prevision_total = pd.DataFrame({
        'semaine': range(1, len(prevision_np_total) + 1),  # First column contains numbers from 1
        'prevision': np.round(prevision_np_total).astype(int)  # Second column contains the NumPy array elements
    })
    # convert the dataframe to a list of dictionaries
    dic_prevision_total = df_prevision_total.to_dict('records')
    # saving the prevision total to database in xlsx file
    xlsx_prevision_total_path = 'prevision_total.xlsx'
    df_prevision_total.to_excel(xlsx_prevision_total_path, index=False)
    xlsx_prevision_total_file = File(open(xlsx_prevision_total_path, 'rb'))
    entrepot_central = Entrepot_central.objects.first()
    entrepot_central.entrp_prevision = xlsx_prevision_total_file
    entrepot_central.save()
    # return the list of dictionaries
    return dic_prevision_total

#-------------------fonction pour envoyer data prevision total en JSON pour le graphique
def prevision_total_json(request):
    entrepot_central = Entrepot_central.objects.first()
    if entrepot_central.entrp_prevision:
        xlsx_prevision_total = entrepot_central.entrp_prevision
        df_prevision_total = pd.read_excel(xlsx_prevision_total)
        dic_prevision_total = df_prevision_total.to_dict('records')
    else:
        dic_prevision_total = caclul_prevision_total()
    prevision_list = [dic['prevision'] for dic in dic_prevision_total if 'prevision' in dic]
    print(prevision_list)
    return JsonResponse(prevision_list, safe=False)

def prevision(request):
    '''
    entrepot_central = Entrepot_central.objects.first()
    if entrepot_central.entrp_prevision:
        xlsx_prevision_total = entrepot_central.entrp_prevision
        df_prevision_total = pd.read_excel(xlsx_prevision_total)
        dic_prevision_total = df_prevision_total.to_dict('records')
    else:
        dic_prevision_total = caclul_prevision_total()
    prevision_list = [dic['prevision'] for dic in dic_prevision_total if 'prevision' in dic]
    '''
    return render(request, 'DRP/prevision.html')

def historique(request):
    form = DepotChoiceForm()
    if request.method == 'POST':
        form = DepotChoiceForm(request.POST)
        if form.is_valid():
            depot = form.cleaned_data['depot']
            hist_data = pd.read_excel(depot.hist_data) # reading the excel file
            hist_data.columns = ['semaine', 'demande'] # renaming the columns
            hist_data = hist_data.to_dict('records') # converting the dataframe to a list of dictionaries
            # returning the data to the template
            return render(request, 'DRP/historique.html', {'form': form, 'hist_data': hist_data})
    return render(request, 'DRP/historique.html', {'form': form})

def planification(request):
    return render(request, 'DRP/planification.html')

#-------------------fonction pour calculer la prévision de depot
def caclul_prevision(dataframe):
    # calcul de la droite de régression
    np_data_array = dataframe.values
    temp = np.cov(np_data_array, rowvar=False) #returns covariance matrix, diagonal is V(x) and V(y) and others is COV(x,y)
    a = temp[0,1] / temp[0,0]
    b = np.mean(np_data_array[:,1]) - (a * np.mean(np_data_array[:,0]) )
    print(f"equation is : {a}*x + {b}")

    x_seq = np_data_array[:,0]
    y_seq = np_data_array[:,1]
    #----------------------- calcule des coefficients saisonières
    # les valeurs de demande théorique d'après le courbe
    y_calculee = a * x_seq + b
    # calcule de tous les coefficients de tous le données historique
    coeff = y_seq / y_calculee
    # initializer array des coefficients saisoniere de chaque semaine de l'année par des zeros
    coeff_week = np.zeros(52)
    # le nbr des semaines qui présente dans les données historique
    nbr_weeks = len(coeff)
    nbr_years = nbr_weeks / 52

    # boucle pour calculer la moyenne de coefficient de chaque semaine de l'année (année comport 52 semaines)
    for i in range(52):
        if i < nbr_weeks:
            if i+52 < nbr_weeks:
                if i+52+52 < nbr_weeks:
                    coeff_week[i] = (coeff[i] + coeff[i+52]+ coeff[i+52+52]) / 3
                else:
                    coeff_week[i] = (coeff[i] + coeff[i+52]) / 2
            else:
                coeff_week[i] = coeff[i]
    print(coeff_week)

    # calcul de la prévision
    #prevision of the next year
    first_week_of_next_year = 157
    prevision_y = np.zeros(52)
    for i in range(52):
        prevision_y[i] = (a*(i+first_week_of_next_year)+b) * coeff_week[i]

    prevision_values = np.round(prevision_y).astype(int)
    df_prevision = pd.DataFrame({
    'weeks': range(1, len(prevision_values) + 1),  # First column contains numbers from 1
    'prevision': prevision_values  # Second column contains the NumPy array elements
    })
    print(df_prevision)
    return df_prevision # returning the df of prevision


def parametre(request):
    # getting the instance of the first entrepot in database
    entrepot_central = Entrepot_central.objects.first()
    # getting the list of depots
    depots_list = Depot.objects.all()

    form_entrepot = EntrepotCentralForm()
    form_depot = DepotForm()
    form_delete_depot = DeleteDepotForm()
    submitted_depot = False
    submitted_entrepot = False
    submitted_delete_depot = False
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'entrepot':
            form_entrepot = EntrepotCentralForm(request.POST, instance=entrepot_central)
            if form_entrepot.is_valid():
                form_entrepot.save()
                return HttpResponseRedirect('/DRP/parametre?submitted_entrepot=True')    
        elif form_type == 'depot':
            form_depot = DepotForm(request.POST, request.FILES)
            if form_depot.is_valid():
                form_depot = form_depot.save(commit=False)
                form_depot.id_entrepot_central = entrepot_central
                # calcul de prévision
                hist_data = pd.read_excel(form_depot.hist_data) # reading the excel file
                hist_data.columns = ['semaine', 'demande'] # renaming the columns
                # appel de fonction de calcul de prévision
                df_prevision = caclul_prevision(hist_data)
                # saving the excel file in database
                xlsx_prevision_path = 'prevision.xlsx'
                df_prevision.to_excel(xlsx_prevision_path, index=False)
                xlsx_prevision_file = File(open(xlsx_prevision_path, 'rb'))
                form_depot.prevision_depot = xlsx_prevision_file
                form_depot.save()
                return HttpResponseRedirect('/DRP/parametre?submitted_depot=True')
        elif form_type == 'delete_depot':
            form_delete_depot = DeleteDepotForm(request.POST)
            if form_delete_depot.is_valid():
                depot = form_delete_depot.cleaned_data['depot']
                depot.delete()
                return HttpResponseRedirect('/DRP/parametre?submitted_delete_depot=True')
    else:
        form_entrepot = EntrepotCentralForm(instance=entrepot_central)
        form_depot = DepotForm()
        form_delete_depot = DeleteDepotForm()
        if 'submitted_entrepot' in request.GET:
            submitted_entrepot = True
        elif 'submitted_depot' in request.GET:
            submitted_depot = True
        elif 'submitted_delete_depot' in request.GET:
            submitted_delete_depot = True

    return render(request, 'DRP/parametre.html' , {'form_entrepot': form_entrepot , 'form_depot': form_depot , 'submitted_entrepot': submitted_entrepot , 'submitted_depot': submitted_depot, 'depots_list': depots_list, 'form_delete_depot': form_delete_depot, 'submitted_delete_depot': submitted_delete_depot})


