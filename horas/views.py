from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Cliente, Lancamento


def lancamentos_por_cliente(cliente, lancamento):
        return Lancamento.objects.filter(cliente=Cliente.objects.get(nome_cliente="oclienteteste")))

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "horas/dashboard.html"
    context_object_name = "lista_clientes_usuario"

    def get_queryset(self):
        return Cliente.objects.filter(usuario=self.request.user)