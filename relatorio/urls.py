from django.urls import path

from . import views

urlpatterns = [
    path('', views.selecao_tabela),
    path('visualizacao/', views.visualizacao, name='visualizacao'),
    
]
