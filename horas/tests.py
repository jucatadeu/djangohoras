import datetime

from django.test import TestCase
from django.db import models
from django.utils import timezone

from .models import Cliente, Lancamento
from contas.models import Usuario



class TestCliente(TestCase):
    def setUp(self):

        Cliente.objects.create(nome_cliente = "oclienteteste")

        Lancamento.objects.create(
            usuario = Usuario.objects.create(username="ousuarioteste"),
            cliente = Cliente.objects.get(nome_cliente="oclienteteste"),
            diahora_inicio = timezone.now() - datetime.timedelta(hours=5),
            diahora_fim = timezone.now(),
        )

    def test_vinculo_lancamento_cliente(self):        
        self.assertTrue(Lancamento.objects.filter(cliente=Cliente.objects.get(nome_cliente="oclienteteste")))
        