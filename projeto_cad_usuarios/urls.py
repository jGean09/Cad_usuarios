
from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, viiew reposável , nome de referencia
    #usuarios.com (criando rota)
    path('',views.home, name="home"),
]
