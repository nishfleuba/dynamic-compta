from django.contrib import admin
from .models import *

@admin.register(PlanComptable)
class PlanComptableAdmin(admin.ModelAdmin):
    list_display = ('numero', 'is_active', 'quantite_unitaire')
    list_filter = ('is_active',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'debiteur', 'crediteur', 'amortissement' , 'is_deleted', 'created_by')
    list_filter = ('is_deleted', 'created_by')
    search_fields = ('nom', 'categorie')

@admin.register(HistoriqueMenu)
class HistoriqueMenuAdmin(admin.ModelAdmin):
    list_display = ('menu', 'created_at', 'created_by', 'motif')
    list_filter = ('created_at', 'created_by')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('menu', 'montant', 'debiteur', 'crediteur', 'created_at', 'created_by')
    list_filter = ('created_at', 'created_by')
    search_fields = ('menu__nom',)
