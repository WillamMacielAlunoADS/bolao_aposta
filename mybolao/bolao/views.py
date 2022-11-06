from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Aposta, Equipe, Partida, User
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

def logar(request):
    return render(request,'bolao/login.html', {})

def usuario(request):
    return render(request,'bolao/index.html', {})

@require_POST
def entrar(request):
    usuario_aux = User.objects.get(email=request.POST['email'])
    usuario = authenticate(username=usuario_aux.username, password=request.POST["senha"])
    if usuario is not None:
        login(request, usuario)
        partida = Partida.objects.all()
        #usuario = User.objects.all()
        return render(request,'bolao/aposta.html', {'partida': partida, 'usuario': usuario})
    return HttpResponseRedirect('/')



@require_POST
def cadastrar_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux:
            return render(request,'bolao/index.html', {})

    except User.DoesNotExist:
        nome_usuario = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']

        novoUsuario = User.objects.create_user(username = nome_usuario, email = email, password = senha)
        novoUsuario.save()
        return render(request,'bolao/login.html', {})

def aposta(request):
    partida = Partida.objects.all()
    usuario = User.objects.all()
    return render(request, 'bolao/aposta.html', {'partida': partida, 'usuario': usuario})

def aposta_edit(request, pk):
    jogo = get_object_or_404(Partida, pk=pk)
    aposta = Aposta.objects.all()
    usuario = User.objects.all()
    return render(request, 'bolao/aposta_edit.html', {'aposta': aposta, 'usuario': usuario, 'jogo': jogo})

def save_aposta(request):
    return print('e')