from django.contrib import admin
from .models import Categoria, ItemCardapio


class ItemInline(admin.TabularInline):
    """Mostra itens dentro da página da categoria."""
    model = ItemCardapio
    extra = 1
    fields = ('nome', 'preco', 'disponivel', 'destaque')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('icone', 'nome', 'ordem')
    list_editable = ('ordem',)
    inlines = [ItemInline]


@admin.register(ItemCardapio)
class ItemCardapioAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'categoria', 'preco',
        'disponivel', 'destaque'
    )
    list_filter = ('categoria', 'disponivel', 'destaque')
    search_fields = ('nome', 'descricao')
    list_editable = ('disponivel', 'destaque')
    list_per_page = 20