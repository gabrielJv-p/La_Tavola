# cardapio_restaurante/urls.py  (urls do PROJETO)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cardapio.urls')),   # delega tudo para o app
]

# Serve arquivos de mídia (imagens) em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
