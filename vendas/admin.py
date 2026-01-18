from django.contrib import admin
from .models import Venda, ItemVenda

# Inline para mostrar os itens da venda dentro da venda
class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1  # quantos campos extras aparecem por padrão

    class Media:
        js = ("vendas/js/itemvenda_default.js",)

# Admin da Venda
@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]  # mostra os itens da venda
    list_display = ("id", "nome_comprador", "forma_pagamento", "valor_total", "data_venda")
    readonly_fields = ("valor_total",)
