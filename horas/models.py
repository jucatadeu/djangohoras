from django.db import models
from contas.models import Usuario

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=50)
    valor_hora = models.PositiveIntegerField()
    """grupo = GRUPO_ECONOMICO"""
    
    def __str__(self):
        return self.nome_cliente