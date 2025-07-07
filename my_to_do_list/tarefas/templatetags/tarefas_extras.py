# tarefas/templatetags/tarefas_extras.py

from django import template
from datetime import datetime

register = template.Library()

@register.filter
def formatDate(value):
    """
    Formata um objeto datetime em uma string legível.
    Exemplo: 2025-07-07 16:53:58 -> 07 de Julho de 2025 às 16:53
    """
    if isinstance(value, datetime):
        # Você pode ajustar o formato da data e hora aqui conforme sua preferência
        return value.strftime("%d de %B de %Y às %H:%M")
    return value # Retorna o valor original se não for um datetime