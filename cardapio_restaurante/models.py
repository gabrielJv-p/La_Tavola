from django.db import models


class Categoria(models.Model):
    """Categorias do cardápio: Entradas, Pratos, etc."""
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    icone = models.CharField(
        max_length=10,
        blank=True,
        help_text="Emoji para representar a categoria"
    )
    ordem = models.PositiveIntegerField(
        default=0,
        help_text="Ordem de exibição no cardápio"
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['ordem', 'nome']

    def __str__(self):
        return f"{self.icone} {self.nome}"


class ItemCardapio(models.Model):
    """Um prato ou bebida do cardápio."""
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='itens'
    )
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(
        upload_to='pratos/',
        blank=True,
        null=True
    )
    disponivel = models.BooleanField(
        default=True,
        help_text="Marque se o item está disponível hoje"
    )
    destaque = models.BooleanField(
        default=False,
        help_text="Exibe o item em destaque no topo"
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Item do Cardápio"
        verbose_name_plural = "Itens do Cardápio"
        ordering = ['categoria', 'nome']

    def __str__(self):
        return f"{self.nome} — R$ {self.preco}"

    def preco_formatado(self):
        return f"R$ {self.preco:.2f}".replace('.', ',')