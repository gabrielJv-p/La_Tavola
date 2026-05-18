from django.urls import path
from . import views

urlpatterns = [
    path('', views.cardapio_home, name='cardapio_home'),
    path('categoria/', views.cadastrar_categoria, name='cadastro_categoria'),
    path('categoria/<int:categoria_id>/excluir/', views.excluir_categoria, name='excluir_categoria'),
    path('item/', views.cadastrar_item, name='cadastro_item'),
    path('item/<int:item_id>/excluir/', views.excluir_item, name='excluir_item'),
]
