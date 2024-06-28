from django.shortcuts import render
from app_cad_usuarios import views
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    #exibir todo em nova da pasta
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retorna os usuarios pra pagina
    return render(request,'usuarios/usuarios.html',usuarios)