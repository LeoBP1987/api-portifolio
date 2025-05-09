from django.contrib import admin
from portifolio.models import UsuariosCustomizados, Tecnologias, Projetos
from markdownx.admin import MarkdownxModelAdmin

class UsuariosCustomizadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'username', 'email')
    list_display_links = ('nome_completo', 'username', 'email')
    list_per_page = 10
    search_fields = ('nome_completo', 'username', 'email')
    ordering = ('username',)

admin.site.register(UsuariosCustomizados, UsuariosCustomizadosAdmin)

class TecnologiasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tipo')
    list_display_links = ('nome', 'tipo')
    list_per_page = 10
    search_fields = ('nome', 'tipo')
    ordering = ('nome',)

admin.site.register(Tecnologias, TecnologiasAdmin)

class ProjetosAdmin(MarkdownxModelAdmin):
    list_display = ('id', 'nome', 'ordem', 'descricaoCurta', 'linkDeploy', 'linkRepositorio')
    list_display_links = ('nome', 'descricaoCurta', 'linkDeploy', 'linkRepositorio')
    list_per_page = 10
    search_fields = ('nome', 'descricaoCurta', 'linkDeploy', 'linkRepositorio')
    ordering = ('nome',)

admin.site.register(Projetos, ProjetosAdmin)