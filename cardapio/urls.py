# cardapio/urls.py  (urls do APP)
from django.urls import path
from . import views

app_name = 'cardapio'

urlpatterns = [
    path('', views.cardapio, name='cardapio'),
    path('categoria/<int:categoria_id>/', views.categoria_detalhe, name='categoria_detalhe'),
    path('item/<int:item_id>/', views.item_detalhe, name='item_detalhe'),
]
