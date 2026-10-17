from django.contrib import admin
from django.urls import path, include, reverse
from . import views

urlpatterns = [
    path("", views.RedirectView.as_view(), name="redirect"),
    path("contas/", include("contas.urls")),
    path('admin/', admin.site.urls),
    path("horas/", include("horas.urls"))
]
