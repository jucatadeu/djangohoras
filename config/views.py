from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class RedirectView(LoginRequiredMixin, generic.RedirectView):
    url = "horas:dashboard"



