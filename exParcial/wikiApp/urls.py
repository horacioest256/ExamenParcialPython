from django.urls import path, include
from . import views

app_name = 'wikiApp'

urlpatterns = [
    path('', views.directorio, name='directorio'),
    path('nuevoTema',views.nuevoTema,name='nuevoTema'),
    path('nuevoArticulo',views.nuevoArticulo,name='nuevoArticulo'),
    path('vistaTema/<str:idTema>',views.vistaTema,name='vistaTema'),
    path('vistaArticulo/<str:idArticulo>',views.vistaArticulo,name='vistaArticulo'),
    path('buscarArticulo', views.buscarArticulo, name='buscarArticulo')
]