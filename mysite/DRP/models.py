from django.db import models

# Create your models here.
class Entrepot_central(models.Model):
    id_entrepot_central = models.AutoField(primary_key=True)
    nom_entrepot_central = models.CharField(max_length=100)
    adresse_entrepot_central = models.CharField(max_length=100)
    telephone_entrepot_central = models.CharField(max_length=100)
    email_entrepot_central = models.CharField(max_length=100)
    entrp_stock = models.IntegerField()
    entrp_prevision = models.FileField(upload_to='prevision_total/')

    def __str__(self):
        return self.nom_entrepot_central

class Depot(models.Model):
    id_depot = models.AutoField(primary_key=True)
    id_entrepot_central = models.ForeignKey(Entrepot_central, on_delete=models.CASCADE)
    nom_depot = models.CharField(max_length=100)
    zone_depot = models.CharField(max_length=100)
    telephone_depot = models.CharField(max_length=100)
    stock_depot = models.IntegerField()
    prevision_depot = models.FileField(upload_to='prevision/')

    def __str__(self):
        return self.nom_depot

class Historique(models.Model):
    id_historique = models.AutoField(primary_key=True)
    id_depot = models.ForeignKey(Depot, on_delete=models.CASCADE)
    hist_data = models.FileField(upload_to='historique/')

    def __str__(self):
        return self.id_historique