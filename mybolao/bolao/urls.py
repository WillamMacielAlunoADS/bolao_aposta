from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.usuario, name='usuario'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('logar/', views.logar, name='logar'),
    path('entrar/', views.entrar, name='entrar'),
    path('', views.aposta, name='aposta'),
    path('aposta_edit/<int:pk>/', views.aposta_edit, name='aposta_edit'),
    path('save_aposta/', views.save_aposta, name='save_aposta'),
]