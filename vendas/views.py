from django.http import JsonResponse
from produtos.models import Produto
from django.shortcuts import get_object_or_404

def get_preco_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    # Aqui escolhemos o preço dependendo do que você quiser
    preco = produto.preco_avista()  # ou preco_prazo()
    return JsonResponse({"preco": float(preco)})