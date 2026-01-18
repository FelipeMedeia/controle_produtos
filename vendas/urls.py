from django.urls import path
from . import views

urlpatterns = [
    path("get_preco_produto/<int:produto_id>/", views.get_preco_produto, name="get_preco_produto"),
]