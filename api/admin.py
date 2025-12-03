from django.contrib import admin,messages
from django.utils import timezone
from .models import *

@admin.register(PlanComptable)
class PlanComptableAdmin(admin.ModelAdmin):
    list_display = ('numero','nom', 'is_active', 'quantite_unitaire')
    list_filter = ('is_active',)

from django.contrib import admin, messages
from .models import Menu, HistoriqueMenu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'debiteur', 'crediteur', 'amortissement', 'is_deleted', 'created_by', 'validate_by')
    list_filter = ('is_deleted', 'created_by')
    search_fields = ('nom', 'categorie')
    actions = ["valider_menu"]
    filter_horizontal = ('permitted_users',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.validate_by = None      
            obj.validate_at = None      
            super().save_model(request, obj, form, change)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "La modification n'est pas autorisée")
            return 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(permitted_users=request.user)

    def has_delete_permission(self, request, obj=None):
        if obj:
            if obj.validate_by or Journal.objects.filter(menu=obj).exists():
                return False 
        return super().has_delete_permission(request, obj)

    def delete_model(self, request, obj):

        if obj.validate_by or Journal.objects.filter(menu=obj).exists():
            messages.error(request, f"Le menu '{obj.nom}' ne peut pas être supprimé car il a été validé ou journalisé.")
            return
        super().delete_model(request, obj)

    def valider_menu(self, request, queryset):

        for menu in queryset:

            if menu.validate_by:
                messages.error(request, f"Le menu '{menu.nom}' est déjà validé.")
                return

            menu.validate_by = request.user
            menu.validate_at = timezone.now()
            menu.save()

            Journal.objects.create(
                menu=menu,
                created_by=request.user,
                debiteur=menu.debiteur,
                crediteur=menu.crediteur,
                amortissement=menu.amortissement
            )

            HistoriqueMenu.objects.create(
                menu=menu,
                created_by=request.user,
                motif=f"Validation du menu {menu.nom}"
            )

        messages.success(request, "Validation effectuée avec succès.")

    valider_menu.short_description = "Valider menu"


@admin.register(HistoriqueMenu)
class HistoriqueMenuAdmin(admin.ModelAdmin):
    list_display = ('menu', 'created_at', 'created_by', 'motif')
    list_filter = ('created_at', 'created_by')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('menu', 'montant', 'debiteur', 'crediteur', 'created_at', 'created_by')
    list_filter = ('created_at', 'created_by')
    search_fields = ('menu__nom',)
