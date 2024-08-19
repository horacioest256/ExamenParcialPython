from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import tema, articulo
# Create your views here.
def directorio(request):
     listaTemas = tema.objects.all().order_by('id')
     listaArticulos = articulo.objects.all()
     return render(request,'directorio.html',{
        'listaTemas':listaTemas,
        'listaArticulos':listaArticulos
    })
        
def nuevoTema(request):
     listaTemas = tema.objects.all().order_by('id')
     if request.method == 'POST':
        nombreTema = request.POST.get('nombre')
        descripcionTema = request.POST.get('descripcion')
        objTema = tema.objects.create(
            nombreTema=nombreTema,
            descripcionTema=descripcionTema
        )
        objTema.save()
        return HttpResponseRedirect(reverse('wikiApp:directorio'))
     return render(request,'nuevoTema.html',{
        'listaTemas':listaTemas
    })
      
     return render(request,'nuevoTema.html')

def nuevoArticulo(request):
     listaArticulos = articulo.objects.all().order_by('id')
     if request.method == 'POST':
        tituloArticulo = request.POST.get('titulo')
        descripcionArticulo = request.POST.get('descripcion')
        temaRelacionado = tema.objects.get(id=temaRegistro)
        objArticulo = articulo.objects.create(
            tituloArticulo=tituloArticulo,
            descripcionArticulo=descripcionArticulo,
            temaRelacionado=temaRelacionado
        )
        objArticulo.save()
        return HttpResponseRedirect(reverse('wikiApp:directorio'))
     return render(request,'nuevoTema.html',{
        'listaArticulos':listaArticulos
    })


def vistaTema(request,idTema):
    listaTemas = tema.objects.all().order_by('id')
    objTemas = tema.objects.get(id=idtemas)
    listaTemas = objDtema.tema_set.all()
    return render(request,'vistaTemas.html',{
        'listaTema':listaTema,
        'objTema':objTema,
        'listaTemas': listaTemas
    })

def vistaArticulo(request,idArticulo):
    listaTemas = tema.objects.all().order_by('id')
    objArticulo = articulo.objects.get(id=idArticulo)
    return render(request,'vistaTema.html',{
        'listaTema':listaArticulos,
        'objArticulo':objArticulo,
    })