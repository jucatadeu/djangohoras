from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente, Lancamento, Grupo


admin.site.register(Cliente)
admin.site.register(Lancamento)
admin.site.register(Grupo)