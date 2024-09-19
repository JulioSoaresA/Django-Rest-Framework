from django.contrib import admin
from escola.models import Estudante, Curso, Matricula

class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome', 'cpf')
    ordering = ('nome',)
    list_per_page = 20


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo',)
    search_fields = ('codigo',)
    list_per_page = 20
    
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso', 'turno', 'data_matricula')
    list_display_links = ('id', 'estudante',)
    search_fields = ('estudante__nome', 'curso__codigo',)
    list_per_page = 20


admin.site.register(Estudante, EstudanteAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Matricula, MatriculaAdmin)