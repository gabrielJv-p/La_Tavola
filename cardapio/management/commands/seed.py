from django.core.management.base import BaseCommand
from cardapio.models import Categoria, ItemCardapio

class Command(BaseCommand):
    help = 'Popula o banco com dados de exemplo do cardápio'

    def handle(self, *args, **kwargs):
        ItemCardapio.objects.all().delete()
        Categoria.objects.all().delete()

        self.stdout.write('Criando categorias...')

        entradas = Categoria.objects.create(nome='Entradas', icone='🥗', ordem=1)
        principais = Categoria.objects.create(nome='Pratos Principais', icone='🍽️', ordem=2)
        bebidas = Categoria.objects.create(nome='Bebidas', icone='🥤', ordem=3)
        sobremesas = Categoria.objects.create(nome='Sobremesas', icone='🍮', ordem=4)

        self.stdout.write('Criando itens...')

        ItemCardapio.objects.create(
            nome='Bruschetta ao Tomate', categoria=entradas,
            descricao='Pão italiano grelhado com tomate e manjericão',
            preco=18.90, disponivel=True, destaque=False
        )
        ItemCardapio.objects.create(
            nome='Bolinho de Bacalhau', categoria=entradas,
            descricao='6 unidades com molho tártaro',
            preco=32.00, disponivel=True, destaque=True
        )
        ItemCardapio.objects.create(
            nome='Frango Grelhado', categoria=principais,
            descricao='Filé de frango grelhado com legumes',
            preco=42.90, disponivel=True, destaque=True
        )
        ItemCardapio.objects.create(
            nome='Filé ao Molho Madeira', categoria=principais,
            descricao='Filé mignon com molho madeira e batatas rústicas',
            preco=89.90, disponivel=True, destaque=True
        )
        ItemCardapio.objects.create(
            nome='Massa ao Sugo', categoria=principais,
            descricao='Espaguete com molho de tomate fresco e manjericão',
            preco=38.00, disponivel=False, destaque=False
        )
        ItemCardapio.objects.create(
            nome='Suco de Laranja', categoria=bebidas,
            descricao='Natural 500ml',
            preco=12.00, disponivel=True, destaque=False
        )
        ItemCardapio.objects.create(
            nome='Refrigerante', categoria=bebidas,
            descricao='Lata 350ml',
            preco=8.00, disponivel=True, destaque=False
        )
        ItemCardapio.objects.create(
            nome='Pudim de Leite', categoria=sobremesas,
            descricao='Receita tradicional da casa',
            preco=22.00, disponivel=True, destaque=True
        )
        ItemCardapio.objects.create(
            nome='Brownie com Sorvete', categoria=sobremesas,
            descricao='Brownie quente com sorvete de creme',
            preco=28.00, disponivel=True, destaque=False
        )

        self.stdout.write(self.style.SUCCESS('✅ Banco populado com sucesso!'))