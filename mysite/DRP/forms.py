# forms.py

from django import forms
from .models import Entrepot_central

class EntrepotCentralForm(forms.ModelForm):
    class Meta:
        model = Entrepot_central
        fields = ['nom_entrepot_central', 'adresse_entrepot_central', 'entrp_stock']
