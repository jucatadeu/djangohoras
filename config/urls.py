from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("contas/", include("contas.urls")),
    path('admin/', admin.site.urls),
    path("horas/", include("horas.urls"))
]
