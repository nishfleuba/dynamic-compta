from django.db import models
from django.contrib.auth.models import User



class PlanComptable(models.Model):
    numero = models.IntegerField()
    is_active = models.BooleanField(default=False)
    quantite_unitaire = models.IntegerField()

    def __str__(self):
        return f"{self.numero}"

class Menu(models.Model):

    nom = models.CharField(max_length=60)
    categorie = models.CharField(max_length=60)
    debiteur = models.ForeignKey(PlanComptable,on_delete=models.PROTECT, related_name='debiteur')
    crediteur = models.ForeignKey(PlanComptable,on_delete=models.PROTECT, related_name='crediteur')
    amortissement = models.ForeignKey(PlanComptable,on_delete=models.PROTECT, related_name='amortissement')
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nom}-{self.debiteur} - {self.crediteur} - {self.amortissement}"

class HistoriqueMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    motif = models.CharField(max_length=255)

    def __str__(self):
        return f"Historique de {self.menu} créé le {self.created_at} par {self.created_by}"