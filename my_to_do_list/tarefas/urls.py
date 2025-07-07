from django.urls import path
from . import views # Importa as views da sua app

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'), # Rota para a página principal da lista de tarefas
    path('api/criar/', views.criar_tarefa_api, name='criar_tarefa_api'), # Rota para a API de criação
    
]