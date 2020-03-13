from django.contrib import admin
from .models import PJT, MR, EQT, PDS, MDS

@admin.register(PJT)
class PJTAdmin(admin.ModelAdmin):
    list_display = ('P_No','P_Name','P_Country','P_Client')
    list_filter = ('P_No','P_Country')

    fieldsets = (
        ('Project', {
            'fields': ('P_No','P_Name','P_Country','P_Client')
        }),
    )

@admin.register(MR)
class MRAdmin(admin.ModelAdmin):
    list_display = ('P_No','M_No','M_Name')

    fieldsets = (
        ('Project', {
            'fields': ('P_No',)
        }),
        ('Requisition', {
            'fields': ('M_No','M_Name')
        }),
    )

@admin.register(EQT)
class EQTAdmin(admin.ModelAdmin):
    list_display = ('P_No','M_No','E_No','E_Name','E_User')

    fieldsets = (
        ('Summary', {
            'fields': ('P_No','M_No')
        }),
        ('Equipment', {
            'fields': ('E_No','E_Name','E_User')
        }),
    )


@admin.register(PDS)
class PDSAdmin(admin.ModelAdmin):
    list_display = ('E_Name', 'PD_Fluid', 'PD_Head', 'PD_Dens', 'PD_NPSH')

@admin.register(MDS)
class MDSAdmin(admin.ModelAdmin):
    list_display = ('E_Name', 'MD_Type', 'MD_Seal', 'MD_Matl')





