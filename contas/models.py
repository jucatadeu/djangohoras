from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nome_usuario = models.CharField(default="", max_length=50)
