from django.views import generic


class RedirectView(generic.RedirectView):
    pattern_name = "horas:dashboard"



