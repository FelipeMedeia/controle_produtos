from django.db import models
from django.utils import timezone
from produtos.models import Produto

class Venda(models.Model):

    FORMA_PAGAMENTO_CHOICES = (("avista", "À Vista"),("parcelado", "Parcelado"),)

    nome_comprador = models.CharField(max_length=150)
    data_venda = models.DateTimeField(default=timezone.now)
    forma_pagamento = models.CharField(max_length=10,choices=FORMA_PAGAMENTO_CHOICES)

    valor_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f"Venda #{self.id} - {self.nome_comprador}"
    
    def calcular_total(self):
        total = sum(item.subtotal() for item in self.itens.all())
        self.valor_total = total
        self.save()
        return total
    

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, related_name="itens",on_delete=models.CASCADE)

    produto = models.ForeignKey(Produto,on_delete=models.PROTECT)

    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.produto.nome}({self.quantidade})"
    
    def subtotal(self):
        return self.quantidade * self.preco_unitario
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if self.venda.forma_pagamento =="avista":
                self.preco_unitario = self.produto.preco_avista()
            else:
                self.preco_unitario = self.produto.preco_prazo()
            
            self.produto.baixar_estoque(self.quantidade)
        
        super().save(*args,**kwargs)

        self.venda.calcular_total
