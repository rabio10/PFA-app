from django import forms
from django.forms import ModelForm
from .models import *

CITY_CHOICES = [
    ('', 'Sélectionner une Ville'),
    ('Casablanca', 'Casablanca'),
    ('Mohammedia', 'Mohammedia'),
    # Add more cities as needed
]
# create a entrepot central form 
class EntrepotCentralForm(ModelForm):
    
    adresse_entrepot_central = forms.ChoiceField(
        choices=CITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Sélectionner la Ville'})
    )
    class Meta:
        model = Entrepot_central
        fields = ('nom_entrepot_central', 'adresse_entrepot_central', 'entrp_stock')
        labels = {
            'nom_entrepot_central': 'Nom Entrepot Central',
            'adresse_entrepot_central': 'Adresse Entrepot Central',
            'entrp_stock': 'Stock Entrepot Central',
        }
        widgets = {
            'nom_entrepot_central': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom Entrepot Central'}),
            'entrp_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock Disponible dans l Entrepôt'}),
        }

# create a depot form
class DepotForm(ModelForm):
    zone_depot = forms.ChoiceField(
        choices=CITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Sélectionner la Ville'})
    )

    class Meta:
        model = Depot
        fields = ('nom_depot', 'zone_depot', 'stock_depot' , 'hist_data')
        labels = {
            'nom_depot': 'Nom Depot',
            'zone_depot': 'Zone Depot',
            'stock_depot': 'Stock Depot',
            'hist_data': 'Historique Data',
        }
        widgets = {
            'nom_depot': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom Depot'}),
            'stock_depot': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock Disponible dans le Depot'}),
            'hist_data': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Historique Data'}),
        }