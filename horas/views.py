from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Cliente


class DashboardView(LoginRequiredMixin, generic.ListView):
    template_name = "horas/dashboard.html"
    context_object_name = "lista_clientes_usuario"

    def get_queryset(self):
        return Cliente.objects.filter(usuario=self.request.user)