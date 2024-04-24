from django.db import models

# Create your models here.
class Entrepot_central(models.Model):
    id_entrepot_central = models.AutoField(primary_key=True)
    nom_entrepot_central = models.CharField(max_length=100)
    adresse_entrepot_central = models.CharField(max_length=100)
    telephone_entrepot_central = models.CharField(max_length=100)
    email_entrepot_central = models.CharField(max_length=100)
    responsable_entrepot_central = models.CharField(max_length=100)
    entrp_stock = models.IntegerField()
    entrp_prevision = models.