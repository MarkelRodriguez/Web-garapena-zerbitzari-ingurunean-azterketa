from django.contrib import admin

from alokairuak.models import Etxea,Pertsona,Alokairua

# Register your models here.
class EtxeaAdmin(admin.ModelAdmin):
    list_display = ['izena','herria','pertsona_kop']

admin.site.register(Etxea,EtxeaAdmin)

class PertsonaAdmin(admin.ModelAdmin):
    list_display = ['dni','izena','abizena','emaila']

admin.site.register(Pertsona,PertsonaAdmin)

class AlokairuaAdmin(admin.ModelAdmin):
    list_display = ['pertsona','etxea','alokairu_data_hasi','alokairu_data_bukatu']

admin.site.register(Alokairua,AlokairuaAdmin)