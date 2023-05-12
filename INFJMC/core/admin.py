from django.contrib import admin
from core.models import Carrera,Docente
# Register your models here.

class CarreraAdmin (admin.ModelAdmin):
    pass
class DocenteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Docente,DocenteAdmin)
