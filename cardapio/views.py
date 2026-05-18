<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.contrib import messages

from .models import Categoria, ItemCardapio
from .forms import CategoriaForm, ItemCardapioForm

def cardapio_home(request):
    """Página principal com todos os itens agrupados por categoria."""
    categorias = Categoria.objects.prefetch_related(
        'itens'
    ).filter(itens__disponivel=True).distinct()

    destaques = ItemCardapio.objects.filter(
        destaque=True,
        disponivel=True
    )

    return render(request, 'cardapio/home.html', {
        'categorias': categorias,
        'destaques': destaques,
    })

def cadastrar_categoria(request):
    if request.method == 'POST':

        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Categoria cadastrada com sucesso!'
                )
            
            return redirect('cadastro_categoria')
        
        else:

            messages.error(
                request,
                'Erro ao cadastrar categoria.'
            )

    else:

        form = CategoriaForm()

    return render(
        request,
        'cadastro_categoria.html',
        {'form': form}
    )

def cadastrar_item(request):
    if request.method == 'POST':
        form = ItemCardapioForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Item cadastrado com Sucesso!'
            )

            return redirect('cadastro_item')
        
        else:
            messages.error(
                request,
                'Erro ao cadastrar item.'
            )
    
    else:
        form = ItemCardapioForm()

    return render(
        request,
        'cadastro_item.html',
        {'form': form}
    )

=======
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
>>>>>>> e52e147827374faca9c1550e8e413281bc3136cc
