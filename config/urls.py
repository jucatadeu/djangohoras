from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.RedirectView.as_view(), name="inicio"),
    path("contas/", include("contas.urls")),
    path('admin/', admin.site.urls),
    path("horas/", include("horas.urls"))
]
