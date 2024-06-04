from django.db import models

# Create your models here.
class Entrepot_central(models.Model):
    id_entrepot_central = models.AutoField(primary_key=True)
    nom_entrepot_central = models.CharField(max_length=100, null=False, blank=False)
    adresse_entrepot_central = models.CharField(max_length=100, null=False, blank=False)
    entrp_stock = models.IntegerField(null=False, blank=False)
    entrp_prevision = models.FileField(upload_to='prevision_total/')

    def __str__(self):
        return self.nom_entrepot_central +" - "+ self.adresse_entrepot_central

class Depot(models.Model):
    id_depot = models.AutoField(primary_key=True)
    id_entrepot_central = models.ForeignKey(Entrepot_central, on_delete=models.DO_NOTHING)
    nom_depot = models.CharField(max_length=100, null=False, blank=False)
    zone_depot = models.CharField(max_length=100, null=False, blank=False)
    stock_depot = models.IntegerField(null=False, blank=False)
    prevision_depot = models.FileField(upload_to='prevision/')
    hist_data = models.FileField(upload_to='historique/',null=True, blank=True)


    def __str__(self):
        return self.nom_depot
