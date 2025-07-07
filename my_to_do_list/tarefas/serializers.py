from rest_framework import serializers
from .models import Tarefa


class TarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'
        read_only_fields = ['data_criacao', 'data_conclusao']
        