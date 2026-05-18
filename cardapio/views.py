from django.shortcuts import render, get_object_or_404
from .models import Categoria, ItemCardapio


def cardapio(request):
    """Página principal: destaques + todos os itens por categoria."""
    categorias = Categoria.objects.prefetch_related('itens').filter(
        itens__disponivel=True
    ).distinct()

    categorias_com_itens = []
    for categoria in categorias:
        itens = categoria.itens.filter(disponivel=True)
        categorias_com_itens.append({
            'categoria': categoria,
            'itens': itens,
        })

    destaques = ItemCardapio.objects.filter(
        disponivel=True,
        destaque=True
    ).select_related('categoria')

    context = {
        'categorias_com_itens': categorias_com_itens,
        'destaques': destaques,
        'titulo_pagina': 'Cardápio',
    }
    return render(request, 'cardapio/cardapio.html', context)


def categoria_detalhe(request, categoria_id):
    """Itens de uma categoria específica. Retorna 404 se não existir."""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    itens = ItemCardapio.objects.filter(categoria=categoria, disponivel=True)

    context = {
        'categoria': categoria,
        'itens': itens,
        'titulo_pagina': categoria.nome,
    }
    return render(request, 'cardapio/categoria_detalhe.html', context)


def item_detalhe(request, item_id):
    """Detalhes de um item + sugestões da mesma categoria."""
    item = get_object_or_404(ItemCardapio, id=item_id, disponivel=True)

    sugestoes = ItemCardapio.objects.filter(
        categoria=item.categoria,
        disponivel=True
    ).exclude(id=item.id)[:3]

    context = {
        'item': item,
        'sugestoes': sugestoes,
        'titulo_pagina': item.nome,
    }
    return render(request, 'cardapio/item_detalhe.html', context)
