# tarefas/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json # Já importado, mas bom ter certeza
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import Tarefa
from .serializers import TarefasSerializer # Já importado, mas bom ter certeza


def lista_tarefas(request):
    tarefas_queryset = Tarefa.objects.all().order_by('-data_criacao')
    serializer = TarefasSerializer(tarefas_queryset, many=True)
    tarefas_data_for_template = serializer.data

    context = {
        'tarefas': tarefas_data_for_template,
    }
    return render(request, 'tarefas/lista_tarefas.html', context)

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def criar_tarefa_api(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TarefasSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) # Corrigido 'erros' para 'errors'
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)