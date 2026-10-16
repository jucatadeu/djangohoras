from django.db import models
from contas.models import Usuario
from django.utils import timezone


class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_grupo


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=50, unique=True)
    valor_hora = models.PositiveIntegerField(default=0, blank=True, null=True)
    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="membros",
    )

    def __str__(self):
        return self.nome_cliente

    
class Lancamento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    diahora_inicio = models.DateTimeField(null=True)
    diahora_fim = models.DateTimeField(null=True)
    horas_totais = models.DurationField(null=True)