from django.shortcuts import render
from django.http import HttpResponseRedirect
import pandas as pd
from .forms import *

# Create your views here.
def DRP_app(request):
    return render(request, 'DRP/generale.html')

def generale(request):
    return render(request, 'DRP/generale.html')

def prevision(request):
    return render(request, 'DRP/prevision.html')

def historique(request):
    return render(request, 'DRP/historique.html')

def planification(request):
    return render(request, 'DRP/planification.html')

def parametre(request):
    # getting the instance of the first entrepot in database
    entrepot_central = Entrepot_central.objects.first()
    # getting the list of depots
    depots_list = Depot.objects.all()

    form_entrepot = EntrepotCentralForm()
    form_depot = DepotForm()
    submitted_depot = False
    submitted_entrepot = False
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
                form_depot.save()
                return HttpResponseRedirect('/DRP/parametre?submitted_depot=True')
    else:
        form_entrepot = EntrepotCentralForm(instance=entrepot_central)
        form_depot = DepotForm()
        if 'submitted_entrepot' in request.GET:
            submitted_entrepot = True
        elif 'submitted_depot' in request.GET:
            submitted_depot = True

    return render(request, 'DRP/parametre.html' , {'form_entrepot': form_entrepot , 'form_depot': form_depot , 'submitted_entrepot': submitted_entrepot , 'submitted_depot': submitted_depot, 'depots_list': depots_list})


