from django.urls import path
from . import views

urlpatterns = [
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    
    path('autor/<int:autor_id>/', views.entradas_por_autor, name='entradas_por_autor'),
    path('autores/', views.lista_autores, name='lista_autores'),
]
