from django.db import models
from django.contrib.auth.models import User



class PlanComptable(models.Model):
    nom = models.CharField(max_length=100)
    numero = models.IntegerField()
    is_active = models.BooleanField(default=False,editable=False)
    quantite_unitaire = models.IntegerField()

    def __str__(self):
        return f"{self.numero}"

class Menu(models.Model):

    nom = models.CharField(max_length=60)
    categorie = models.CharField(max_length=60)
    debiteur = models.ForeignKey(PlanComptable,on_delete=models.PROTECT, related_name='debiteur')
    crediteur = models.ForeignKey(PlanComptable,on_delete=models.PROTECT, related_name='crediteur')
    amortissement = models.ForeignKey(PlanComptable,on_delete=models.PROTECT, related_name='amortissement')
    is_deleted = models.BooleanField(default=False,editable=False)
    validate_by = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True,related_name='validate',editable=False)
    validate_at = models.DateTimeField(null=True,blank=True,editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,editable=False)
    permitted_users = models.ManyToManyField(User, blank=True, related_name='menus_permis')

    def __str__(self):
        return f"{self.nom}-{self.debiteur} - {self.crediteur} - {self.amortissement}"

class Journal(models.Model):

    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    montant = models.DecimalField(max_digits=12, decimal_places=2,null=True)
    debiteur = models.ForeignKey(PlanComptable, on_delete=models.PROTECT, related_name='journal_debiteur')
    crediteur = models.ForeignKey(PlanComptable, on_delete=models.PROTECT, related_name='journal_crediteur')
    amortissement = models.ForeignKey(PlanComptable, on_delete=models.PROTECT, related_name='journal_amortissement')
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,editable=False)

    def __str__(self):
        return f"{self.menu.nom} - {self.montant}-{self.debiteur} - {self.crediteur}"

class HistoriqueMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,editable=False)
    motif = models.CharField(max_length=255)

    def __str__(self):
        return f"Historique de {self.menu} créé le {self.created_at} par {self.created_by}"

