from django import forms
from .models import Categoria, ItemCardapio


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nome', 'icone', 'ordem']


class ItemCardapioForm(forms.ModelForm):

    class Meta:
        model = ItemCardapio
        fields = [
            'categoria',
            'nome',
            'descricao',
            'preco',
            'disponivel',
            'destaque'
        ]