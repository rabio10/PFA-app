from django import forms
from django.forms import ModelForm
from .models import *

# ----------------------forms in parametre page----------------------
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
        widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Sélectionner la Ville'}),
        label='Ville Entrepôt Central'
    )
    class Meta:
        model = Entrepot_central
        fields = ('nom_entrepot_central', 'adresse_entrepot_central', 'entrp_stock')
        labels = {
            'nom_entrepot_central': 'Nom Entrepôt Central',
            'adresse_entrepot_central': 'Ville Entrepot Central',
            'entrp_stock': 'Stock Entrepôt Central',
        }
        widgets = {
            'nom_entrepot_central': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom Entrepot Central'}),
            'entrp_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock Disponible dans l Entrepôt'}),
        }

# create a depot form
class DepotForm(ModelForm):
    zone_depot = forms.ChoiceField(
        choices=CITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Sélectionner la Ville'}),
        label='Ville Dépôt'
    )

    class Meta:
        model = Depot
        fields = ('nom_depot', 'zone_depot', 'stock_depot' , 'hist_data')
        labels = {
            'nom_depot': 'Nom Dépôt',
            'zone_depot': 'Ville Dépôt',
            'stock_depot': 'Stock Dépôt',
            'hist_data': 'Données Historique (min 1 an, max 3 ans en format xlsx)',
        }
        widgets = {
            'nom_depot': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom Depot'}),
            'stock_depot': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock Disponible dans le Depot'}),
            'hist_data': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Historique Data'}),
        }

#----------------------forms in historique page----------------------

class DepotChoiceForm(forms.Form):
    depot = forms.ModelChoiceField(
        queryset=Depot.objects.all(),
        empty_label='Sélectionner un Dépôt',
        widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Sélectionner un Dépôt'}),
        label='Dépôt à afficher l historique'
        )
    class Meta:
        fields = ('depot',)
        labels = {
            'depot': 'Dépôt à afficher l historique',
        }