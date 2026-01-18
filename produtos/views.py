from django.shortcuts import render
from .models import Produto
from django.db.models import Sum, F, FloatField

def relatorio_estoque(request):
    marcas = Produto.objects.values_list('marca', flat=True).distinct()
    relatorio = []
    total_geral_q = 0
    total_geral_v = 0

    for marca in marcas:
        produtos_queryset = Produto.objects.filter(marca=marca, quantidade_estoque__gt=0)
        if not produtos_queryset.exists():
            continue  # pula marcas sem produtos disponíveis

        produtos = []
        total_quantidade = 0
        total_valor = 0

        for p in produtos_queryset:
            subtotal = float(p.quantidade_estoque) * float(p.preco_descontado)
            produtos.append({
                'nome': p.nome,
                'quantidade_estoque': p.quantidade_estoque,
                'preco_base': p.preco_normal,
                'preco_normal': p.preco_descontado,
                'subtotal': subtotal,
                'foto_url': p.foto.url if p.foto else None
            })
            total_quantidade += p.quantidade_estoque
            total_valor += subtotal

        total_geral_q += total_quantidade
        total_geral_v += total_valor

        relatorio.append({
            'marca': marca,
            'produtos': produtos,
            'total_quantidade': total_quantidade,
            'total_valor': total_valor,
        })

    return render(request, "produtos/relatorio_estoque.html", {
        "relatorio": relatorio,
        "total_geral_q": total_geral_q,
        "total_geral_v": total_geral_v
    })
