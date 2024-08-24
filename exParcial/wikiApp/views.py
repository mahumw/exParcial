from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def nuevo_tema(request):
    return render(request, 'nuevo_tema.html')

def nuevo_articulo(request):
    return render(request, 'nuevo_articulo.html')

def articulo_tema(request):
    return render(request, 'articulo_tema.html')

def articulos(request):
    return render(request, 'articulos.html')

def busqueda(request):
    return render(request, 'busqueda.html')







