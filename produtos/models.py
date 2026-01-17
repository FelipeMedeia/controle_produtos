from django.db import models
from django.utils import timezone

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100,blank=True,null=True)
    tamanho = models.CharField(max_length=50,blank=True,null=True)

    preco_normal = models.DecimalField(max_digits=10,decimal_places=2)
    preco_descontado = models.DecimalField(max_digits=10,decimal_places=2,null=True)

    quantidade_estoque = models.PositiveIntegerField(default=0)
    data_validade = models.DateField(blank=True,null=True)

    foto = models.ImageField(upload_to="produtos/",blank=True,null=True)

    criado_em = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.nome
    
    def preco_avista(self):
        return self.preco_descontado or self.preco_normal
    
    def preco_prazo(self):
        return self.preco_normal
    
    def baixar_estoque(self, quantidade):
        if quantidade > self.quantidade_estoque:
            raise ValueError("Estoque insuficiente!")
        self.quantidade_estoque-=quantidade
        self.save()
