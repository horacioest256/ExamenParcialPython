from django.shortcuts import render

# Create your views here.
def directorio(request):
    return render(request,'directorio.html')
        
def nuevoTema(request):
     return render(request,'nuevoTema.html')

def nuevoArticulo(request):
     return render(request,'nuevoArticulo.html')