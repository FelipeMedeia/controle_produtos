from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ["nome"]
    list_display = ('nome', 'marca', 'categoria', 'quantidade_estoque', 'preco_normal', 'genero', 'imagem_preview')


    def imagem_preview(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="60" height="60" />', obj.foto.url)
        return "Sem foto"
    
    imagem_preview.short_description = "Foto"

    def relatorio_link(self, obj):
        url = reverse('relatorio_estoque')
        return format_html('<a class="button" href="{}" target="_blank">Relatório Estoque</a>', url)
    relatorio_link.short_description = "Relatório"
