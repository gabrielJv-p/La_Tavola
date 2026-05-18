from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Prefetch
from .models import Categoria, ItemCardapio
from .forms import CategoriaForm, ItemCardapioForm


def cardapio_home(request):
    categorias = Categoria.objects.prefetch_related('itens').filter(
        itens__disponivel=True
    ).distinct()

    destaques = ItemCardapio.objects.filter(destaque=True, disponivel=True)

    return render(request, 'cardapio/home.html', {
        'categorias': categorias,
        'destaques': destaques,
    })


def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('cadastro_categoria')
        else:
            messages.error(request, 'Erro ao cadastrar categoria.')
    else:
        form = CategoriaForm()

    categorias = Categoria.objects.prefetch_related('itens').all()
    return render(request, 'cardapio/cadastro_categoria.html', {
        'form': form,
        'categorias': categorias,
    })


def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method != 'POST':
        return redirect('cadastro_categoria')

    if categoria.itens.exists():
        messages.error(
            request,
            f'Não foi possível remover "{categoria.nome}" porque existem itens cadastrados nela. Remova os itens primeiro.'
        )
        return redirect('cadastro_categoria')

    nome = categoria.nome
    categoria.delete()
    messages.success(request, f'Categoria "{nome}" removida com sucesso!')
    return redirect('cadastro_categoria')


def cadastrar_item(request):
    if request.method == 'POST':
        form = ItemCardapioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item cadastrado com sucesso!')
            return redirect('cadastro_item')
        else:
            messages.error(request, 'Erro ao cadastrar item.')
    else:
        form = ItemCardapioForm()

    itens = ItemCardapio.objects.select_related('categoria').order_by('categoria__ordem', 'categoria__nome', 'nome')
    return render(request, 'cardapio/cadastro_item.html', {
        'form': form,
        'itens': itens,
    })


def excluir_item(request, item_id):
    item = get_object_or_404(ItemCardapio, id=item_id)

    if request.method != 'POST':
        return redirect('cadastro_item')

    nome = item.nome
    item.delete()
    messages.success(request, f'Item "{nome}" removido com sucesso!')
    return redirect('cadastro_item')
