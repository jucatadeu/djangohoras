from django.db import models
from contas.models import Usuario

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=50)
    valor_hora = models.PositiveIntegerField()
    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="membros",
    )
    
    def __str__(self):
        return self.nome_cliente

class Grupo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome