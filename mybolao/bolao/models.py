from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Grupo(models.Model):
    nomeGrupo = models.CharField(max_length = 10, verbose_name='Nome Grupo', unique=True, null=True, blank=False)

    def __str__(self):
        return f'Grupo {self.nomeGrupo}'

class Equipe(models.Model):
    nome = models.CharField(max_length = 100, unique=True, null=True, blank=False)
    grupo = models.ForeignKey(Grupo, related_name='Grupo', null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.grupo}'

class Partida(models.Model):
    equipe1 = models.ForeignKey(Equipe, related_name='equipe1', on_delete=models.CASCADE)
    equipe2 = models.ForeignKey(Equipe, related_name='equipe2', on_delete=models.CASCADE)
    valorAposta = models.FloatField(null=True, blank=False)
    data_criada = models.DateTimeField(default=None, verbose_name='Data Criada')
    data_partida = models.DateTimeField(default=None, verbose_name='Data Partida')
    concluido = models.BooleanField(default=False)
    encerrado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.equipe1.nome} vs {self.equipe2.nome}'

class Aposta(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    placar1 = models.IntegerField(unique=True, null=True, blank=False)
    placar2 = models.IntegerField(unique=True, null=True, blank=False)
    jogo = models.ForeignKey(Partida, related_name='jogo', null=True, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        usuario = str(self.user)
        return usuario








