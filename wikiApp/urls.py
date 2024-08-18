from django.urls import path, include
from . import views

app_name = 'wikiApp'

urlpatterns = [
    path('', views.directorio, name='directorio'),
    path('nuevoTema',views.nuevoTema,name='nuevoTema'),
    path('nuevoArticulo',views.nuevoArticulo,name='nuevoArticulo'),
    #path('vistaDepartamento/<str:idDepartamento>',views.vistaDepartamento,name='vistaDepartamento'),
    #path('vistaUsuario/<str:idPersona>',views.vistaUsuario,name='vistaUsuario')
]