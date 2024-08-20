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
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        objTema = tema.objects.create(
            nombre=nombre,
            descripcion=descripcion
        )
        objTema.save()
        return HttpResponseRedirect(reverse('wikiApp:directorio'))
     return render(request,'nuevoTema.html',{
        'listaTemas':listaTemas
    })
      
     return render(request,'nuevoTema.html')

def nuevoArticulo(request):
     listaTemas = tema.objects.all().order_by('id')
     if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido= request.POST.get('contenido')
        articuloTema = request.POST.get('temaSeleccionado')
        temaRelacionado = tema.objects.get(id=articuloTema)
        objArticulo = articulo.objects.create(
            titulo=titulo,
            contenido=contenido,
            temaRelacionado=temaRelacionado
        )
        objArticulo.save()
        return HttpResponseRedirect(reverse('wikiApp:directorio'))
     return render(request,'nuevoArticulo.html',{
        'listaTemas':listaTemas
    })


def vistaTema(request,idTema):
    listaTemas = tema.objects.all().order_by('id')
    objTema = tema.objects.get(id=idTema)
    listaArticulos = objTema.articulo_set.all()
    return render(request,'vistaTema.html',{
        'listaTemas':listaTemas,
        'objTema':objTema,
        'listaArticulos': listaArticulos
    })

def vistaArticulo(request,idArticulo):
    listaTemas = tema.objects.all().order_by('id')
    objArticulo = articulo.objects.get(id=idArticulo)
    return render(request,'vistaArticulo.html',{
        'listaTemas':listaTemas,
        'objArticulo':objArticulo
    })

