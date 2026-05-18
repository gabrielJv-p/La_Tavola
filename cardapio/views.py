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

