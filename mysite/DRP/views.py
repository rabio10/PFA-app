import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse , FileResponse
import pandas as pd
from .forms import *
import numpy as np
from django.core.files import File

# Create your views here.
def DRP_app(request):
    return render(request, 'DRP/generale.html')

def generale(request):
    entrepot_central = Entrepot_central.objects.first()
    if entrepot_central.entrp_prevision:
        # get the xlsx file of prevision total of entrepot central and convert it to a dataframe
        xlsx_prevision_total = entrepot_central.entrp_prevision
        df_prevision_total = pd.read_excel(xlsx_prevision_total)
        df_prevision_total.columns = ['semaine', 'prevision']
        dic_prevision_total = df_prevision_total.to_dict('records')
    else:
        dic_prevision_total = caclul_prevision_total()
        dic_prevision_total = df_prevision_total.to_dict('records')
    # get the xlsx file of historique total of all depots and convert it to a dataframe
    depots = Depot.objects.all()
    hist_data_total = pd.DataFrame()
    # check if there's a depot instance in the database
    if depots:
        for depot in depots:
            hist_data = pd.read_excel(depot.hist_data)
            hist_data.columns = ['semaine', 'demande']
            # we sum the demandes of all depots to get the total demandes
            hist_data_total = hist_data_total.add(hist_data, fill_value=0)
        hist_data_total = hist_data_total.to_dict('records')
    
    #prevision_list = [dic['prevision'] for dic in dic_prevision_total if 'prevision' in dic]
    #print(prevision_list)
    dic_prevision_total_json = json.dumps(dic_prevision_total)
    hist_data_total_json = json.dumps(hist_data_total)
    return render(request, 'DRP/generale.html', {'dic_prevision_total': dic_prevision_total, 'dic_prevision_total_json': dic_prevision_total_json, 'hist_data_total': hist_data_total, 'hist_data_total_json': hist_data_total_json})

#-------------------fonction pour calculer la prévision total de entrepot central
def caclul_prevision_total():
    depots = Depot.objects.all()
    prevision_np_total = np.zeros(52)
    # get the xlsx files of previons of all depots and convert them to dataframes and then to np arrays
    for depot in depots:
        prevision_df = pd.read_excel(depot.planning_depot)
        prevision_df.columns = ['semaine', 'prevision', 'stock', 'commandes']
        prevision_np = prevision_df.values
        prevision_np = prevision_np[1:,3]
        prevision_np_total = prevision_np_total + prevision_np
    # convert the np array of prevision total to a dataframe
    df_prevision_total = pd.DataFrame({
        'semaine': range(1, len(prevision_np_total) + 1),  # First column contains numbers from 1
        'prevision': np.round(prevision_np_total).astype(int)  # Second column contains the NumPy array elements
    })
    # convert the dataframe to a list of dictionaries
    print(prevision_np_total)
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
    dic_prevision_total = caclul_prevision_total()
    #prevision_list = [dic['prevision'] for dic in dic_prevision_total if 'prevision' in dic]
    #print(prevision_list)
    dic_prevision_total_json = json.dumps(dic_prevision_total)
    return render(request, 'DRP/prevision.html',{'dic_prevision_total': dic_prevision_total, 'dic_prevision_total_json': dic_prevision_total_json})

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
#-------------------fonction pour calculer la plannification et afficher
def make_planning_depot(depot): # returns a list of dictionaries of the planning dataframe and saving xlsx to database
    # getting the stock of the depot
    stock = depot.stock_depot
    # calculating the delay to receive the command of the depot
    delays = np.array([
        [1, 1, 1, 1, 2, 2, 1, 4, 1, 2, 1, 1, 4],
        [1, 1, 1, 1, 1, 2, 1, 4, 1, 1,1, 1, 4],
        [1 ,1, 1, 2, 4, 1, 2, 4, 2, 4, 1, 1, 4],
        [1, 1, 2, 1, 1, 4, 1, 2, 1, 1, 2, 1, 4],
        [2, 1 ,4, 1, 1, 4, 1, 4, 1, 1 ,2, 2 ,4],
        [2, 2, 1, 4, 4, 1, 4, 4, 4, 4, 1 ,2, 4],
        [1, 1, 2 ,1 ,1, 4, 1, 2, 1 ,2, 2, 1, 4],
        [4, 4, 4, 2, 4, 4, 2, 1, 4,4 ,4 ,4 ,4],
        [1 ,1 ,2 ,1 ,1 ,4 ,1, 4, 1, 1 ,1 ,1 ,4],
        [2, 1, 4, 1 ,1, 4, 2, 4, 1, 1 ,4, 2 ,4],
        [1, 1 ,1, 2 ,2 ,1 ,2 ,4 ,1 ,4, 1 ,1, 4],
        [1, 1, 1, 1, 2 ,2, 1, 4, 1, 2 ,1 ,1 ,4],
        [4, 4 ,4 ,4, 4 ,4 ,4, 4 ,4 ,4 ,4 ,4, 1]
    ])
    # Convert the delays matrix to a pandas DataFrame for better readability
    cities = ["Casablanca", "Rabat", "Marrakech", "Fès", "Tanger", "Agadir", "Meknès", "Oujda", "Kénitra", "Tétouan", "Safi", "Mohammédia", "Laayoun"]
    delays_df = pd.DataFrame(delays, index=cities, columns=cities)
    # getting the instance of the first entrepot in database
    entrepot_central = Entrepot_central.objects.first()
    # getting the city of entrepot central
    city_entrepot_central = entrepot_central.adresse_entrepot_central
    # determining the delay to receive the command of the depot depending of the city of the depot and entrepot central
    delay = delays_df.loc[city_entrepot_central, depot.adresse_depot]
    #-------------------calcul de la planification
    # getting the xlsx file of prevision of the depot and convert it to a dataframe
    prevision = pd.read_excel(depot.prevision_depot)
    prevision.columns = ['semaine', 'prevision']
    # making the planning dataframe
    planning_df = pd.DataFrame({
        'semaine': range(1, 53),  # First column contains numbers from 1 to 52
        'prevision': prevision['prevision'],  # Second column contains the prevision values
        'stock': np.full(52, 0),  # Third column contains now empty strings
        'commandes': np.full(52, 0)  # Third column contains the demandes values empty strings
    })
    # inserting first row of the planning dataframe
    initial_row = pd.DataFrame({
        'semaine': [0],
        'prevision': [0],
        'stock': [stock],
        'commandes':[0]
    })
    # concatenate it
    planning_df = pd.concat([initial_row, planning_df]).reset_index(drop=True)
    # filling the planification dataframe
    # iterate through all rows
    for i in range(1,53):
        stock = planning_df.iloc[i-1,2] - planning_df.iloc[i,1]
        if stock > 0:
            planning_df.iloc[i,2] = stock
        else:
            # lets make commande in the week before and register the stock
            cmd = 50 # quantité de approv. de base
            j = 1
            while stock < -cmd: # trouver la quantité de commande necessaire
                cmd = 50 * j
                j += 1
            planning_df.iloc[i,2] = stock + cmd
            planning_df.iloc[i-delay,3] = cmd
    # saving the planning dataframe to a xlsx file
    print(planning_df) # printing the planning dataframe for DEBBUGGING
    xlsx_planning_path = 'planning_depot.xlsx'
    planning_df.to_excel(xlsx_planning_path, index=False)
    xlsx_planning_file = File(open(xlsx_planning_path, 'rb'))
    # saving the xlsx file in the database
    depot.planning_depot = xlsx_planning_file
    depot.save()
    return planning_df.to_dict('records')

def make_planning_entrepot(entrepot): # returns a list of dictionaries of the planning dataframe and saving xlsx to database
    # getting the stock of the entrepot
    stock = entrepot.entrp_stock
    # stock of the entrepot
    stock = entrepot.entrp_stock
    # delay to receive the command of the entrepot
    delay = 1
    # getting the prevision of the entrepot
    prevision = pd.read_excel(entrepot.entrp_prevision)
    prevision.columns = ['semaine', 'prevision']
    # making the planning dataframe
    planning_df = pd.DataFrame({
        'semaine': range(1, 53),  # First column contains numbers from 1 to 52
        'prevision': prevision['prevision'],  # Second column contains the prevision values
        'stock': np.full(52, 0),  # Third column contains now empty strings
        'commandes': np.full(52, 0)  # Third column contains the demandes values empty strings
    })
    # inserting first row of the planning dataframe
    initial_row = pd.DataFrame({
        'semaine': [0],
        'prevision': [0],
        'stock': [stock],
        'commandes':[0]
    })
    # concatenate it
    planning_df = pd.concat([initial_row, planning_df]).reset_index(drop=True)
    # filling the planification dataframe
    # iterate through all rows
    for i in range(1,53):
        stock = planning_df.iloc[i-1,2] - planning_df.iloc[i,1]
        if stock > 0:
            planning_df.iloc[i,2] = stock
        else:
            # lets make commande in the week before and register the stock
            cmd = 50 # quantité de approv. de base
            j = 1
            while stock < -cmd: # trouver la quantité de commande necessaire
                cmd = 50 * j
                j += 1
            planning_df.iloc[i,2] = stock + cmd
            planning_df.iloc[i-delay,3] = cmd
    # saving the planning dataframe to a xlsx file
    print(planning_df) # printing the planning dataframe for DEBBUGGING
    xlsx_planning_path = 'planning_entrepot.xlsx'
    planning_df.to_excel(xlsx_planning_path, index=False)
    xlsx_planning_file = File(open(xlsx_planning_path, 'rb'))
    # saving the xlsx file in the database
    entrepot.entrp_planning = xlsx_planning_file
    entrepot.save()
    return planning_df.to_dict('records')

DEPOT_OF_CHOICE = None

def planification(request):
    # calculating the planning of entrepot central
    entrepot_central = Entrepot_central.objects.first()
    planning_entrepot = make_planning_entrepot(entrepot_central)
    # making the form to choose the depot
    form = DepotChoiceForm()
    if request.method == 'POST':
        form = DepotChoiceForm(request.POST)
        if form.is_valid():
            depot = form.cleaned_data['depot']
            global DEPOT_OF_CHOICE
            DEPOT_OF_CHOICE = depot
            # calling the function of making the planning of the depot
            # if the depot has prevision
            
            planning = make_planning_depot(depot)
            # dictionnary to json
            planning_json = json.dumps(planning)
            # returning the data to the template
            return render(request, 'DRP/planification.html', {'form': form, 'planning_json': planning_json, 'planning': planning, 'planning_entrepot': planning_entrepot})
    
    return render(request, 'DRP/planification.html',{'form': form, 'planning_entrepot': planning_entrepot})

# download planning depot
def download_planning_depot(request):
    depot = Depot.objects.get(id_depot=DEPOT_OF_CHOICE.id_depot)
    file_path = depot.planning_depot.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='planning_depot.xlsx')

# download planning entrepot
def download_planning_total(request):
    entrepot_central = Entrepot_central.objects.first()
    file_path = entrepot_central.entrp_planning.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='planning_entrepot.xlsx')

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
                # calcule de la planification
                make_planning_depot(form_depot)
                # calculer la prévision total
                #caclul_prevision_total()
                #calculer la planification de entrepot central
                #make_planning_entrepot(entrepot_central)
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


