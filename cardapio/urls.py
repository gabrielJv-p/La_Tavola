<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.cardapio_home,
        name='cardapio_home'
    ),

    path(
        'categoria/',
        views.cadastrar_categoria,
        name='cadastro_categoria'
    ),

    path(
        'item/',
        views.cadastrar_item,
        name='cadastro_item'
    ),
]
=======
# cardapio/urls.py  (urls do APP)
from django.urls import path
from . import views

app_name = 'cardapio'

urlpatterns = [
    path('', views.cardapio, name='cardapio'),
    path('categoria/<int:categoria_id>/', views.categoria_detalhe, name='categoria_detalhe'),
    path('item/<int:item_id>/', views.item_detalhe, name='item_detalhe'),
]
>>>>>>> e52e147827374faca9c1550e8e413281bc3136cc
