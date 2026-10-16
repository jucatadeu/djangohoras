from django.urls import path
from . import views

app_name = "horas"
urlpatterns = [
    path("dashboard/", views.IndexView.as_view(), name="dashboard"),
    ]