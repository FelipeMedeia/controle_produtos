from django.contrib import admin
from django.utils.html import format_html
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'marca',
        'quantidade_estoque',
        'preco_normal',
        'genero',
        'imagem_preview'
    )

    def imagem_preview(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" width="60" height="60" />',
                obj.foto.url
            )
        return "Sem foto"

    imagem_preview.short_description = "Foto"
