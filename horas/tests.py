import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import Cliente, Lancamento
from contas.models import Usuario

class TestLancamento(TestCase):
    def setUp(self):

        self.cliente_teste = Cliente.objects.create(nome_cliente = "cliente_teste")
        self.usuario_teste = Usuario.objects.create(username="usuario_teste")

        self.agora = timezone.now()
        self.lancamento_teste = Lancamento.objects.create(
                usuario = self.usuario_teste,
                cliente = self.cliente_teste,
                diahora_inicio = self.agora - datetime.timedelta(hours=5),
                diahora_fim = self.agora,
            )


    def test_vinculo_lancamento_cliente(self):
        self.assertEqual(self.lancamento_teste.cliente, self.cliente_teste)


    def test_calculo_horas_totais(self):
        self.lancamento_teste.diahora_inicio = self.agora - datetime.timedelta(hours=3)
        self.lancamento_teste.save()
        self.lancamento_teste.refresh_from_db()

        self.assertEqual(self.lancamento_teste.horas_totais, datetime.timedelta(hours=3))


    def test_diahorafim_nulo(self):
        self.lancamento_teste.diahora_fim = None
        self.lancamento_teste.save()
        self.lancamento_teste.refresh_from_db()

        self.assertIsNone(self.lancamento_teste.horas_totais)


    def test_clean_fim_vazio(self):
        lancamento = Lancamento(
            usuario=self.usuario_teste,
            cliente=self.cliente_teste,
        )
        lancamento.full_clean()


    def test_clean_fim_antes_inicio(self):
        self.lancamento_teste.diahora_inicio = self.agora + datetime.timedelta(hours=5)

        with self.assertRaises(ValidationError) as contexto:
            self.lancamento_teste.full_clean()

        self.assertIn("diahora_fim", contexto.exception.message_dict)


    def test_clean_fim_igual_inicio(self):
        self.lancamento_teste.diahora_inicio = self.agora

        with self.assertRaises(ValidationError) as contexto:
            self.lancamento_teste.full_clean()

        self.assertIn("diahora_fim", contexto.exception.message_dict)

        