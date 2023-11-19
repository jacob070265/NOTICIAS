from django.contrib import admin
from .models import Noticias,Temas

# Register your models here.

class NoticiasAdmin(admin.ModelAdmin):
    fieldsets = [
('publicacion', {'fields': ['pub_date']}),
('cuerpo', {'fields': ['titulo', 'descripcion']}),
('fotos', {'fields': ['foto1', 'foto2']}),
('temaFK', {'fields': ['tema']}),

    ]

class TemasAdmin(admin.ModelAdmin):
    fields = ['titulo_tema']

admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Temas, TemasAdmin)