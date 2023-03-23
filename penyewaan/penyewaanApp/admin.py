from django.contrib import admin
from . models import Pasar, Penyewa

# Register your models here.
class peyewaanAdmin(admin.ModelAdmin):
    list_display = ('tempat','nama','tipe','blok','nomor','limit','harga','created')
    
class pasarAdmin(admin.ModelAdmin):
    list_display = ('lokasi','created')

admin.site.register(Pasar,pasarAdmin)
admin.site.register(Penyewa,peyewaanAdmin)

admin.site.site_header= 'DINAS PERDAGANGAN'