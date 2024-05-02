from django.urls import path

from . import views

urlpatterns = [
    path('seleciona/', views.selecao_tabela),
    path('visualizacao/', views.visualizacao, name='visualizacao'),
    
]
