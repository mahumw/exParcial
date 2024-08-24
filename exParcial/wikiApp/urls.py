from django.urls import path

from wikiApp import views

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('nuevo_tema/', views.nuevo_tema, name='nuevo_tema'),
    path('nuevo_articulo/', views.nuevo_articulo, name='nuevo_articulo'),
    path('articulo_tema/', views.articulo_tema, name='articulo_tema'),
    path('articulos/', views.articulos, name='articulos'),
    path('busqueda/', views.busqueda, name='busqueda'),
    

    


]