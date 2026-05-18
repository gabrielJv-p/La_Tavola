# Create your models here.
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.CharField(max_length=10, blank=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem', 'nome']

    def __str__(self):
        return self.nome


class ItemCardapio(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='itens'
    )
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome