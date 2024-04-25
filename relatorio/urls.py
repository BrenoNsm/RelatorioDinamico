from django.urls import path

from . import views

urlpatterns = [
    path('', views.teste, name="teste"),
    path('tabelas/', views.exibir_tabelas, name="listadetabela")
]
