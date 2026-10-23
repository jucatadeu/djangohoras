from django.db import models
from django.conf import settings
from django import forms

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
        related_name="clientes_do_usuario",
        blank=True,
    )

    def __str__(self):
        return self.nome_cliente

    
class Lancamento(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="lancamentos",
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="lancamentos", 
    )

    diahora_inicio = models.DateTimeField(null=True)
    diahora_fim = models.DateTimeField(null=True)
    horas_totais = models.DurationField(null=True)


    def save(self, *args, **kwargs):
        if self.diahora_fim is None or self.diahora_inicio is None:
            self.horas_totais = None 
        else:
            self.horas_totais = self.diahora_fim - self.diahora_inicio
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente.nome_cliente}, {self.diahora_inicio}, {self.usuario}"