from django.db import models
from contas.models import Usuario
from django.conf import settings

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
    
    usuarios = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="clientes_selecionados",
        blank=True,
    )

    def __str__(self):
        return self.nome_cliente

    
class Lancamento(models.Model):
    usuario = settings.AUTH_USER_MODEL
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="lancametos", 
    )
    diahora_inicio = models.DateTimeField(null=True)
    diahora_fim = models.DateTimeField(null=True)
    horas_totais = models.DurationField(null=True)

    def save(self, *args, **kwargs):
        self.horas_totais = self.diahora_fim - self.diahora_inicio
        self.save(*args, **kwargs)