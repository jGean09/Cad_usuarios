from django.shortcuts import render
from app_cad_usuarios import views

# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')
