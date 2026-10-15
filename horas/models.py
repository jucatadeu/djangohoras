from django.db import models
from contas.models import Usuario

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.nome_cliente