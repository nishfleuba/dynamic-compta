from django.db import models
from django.contrib.auth.models import User



class PlanComptable(models.Model):
    numero = models.IntegerField()
    is_active = models.BooleanField(default=False)
    quantite = models.IntegerField()

class Menu(models.Model):

    nom = models.CharField(max_length=60)
    categorie = models.CharField(max_length=60)
    debiteur = models.ForeignKey(PlanComptable)
    crediteur = models.ForeignKey(PlanComptable)
    amortissement = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class HistoriqueMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    motif = models.CharField()
