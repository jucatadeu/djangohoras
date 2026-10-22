from django.test import TestCase
from django.conf import settings
from .models import Usuario
from django.shortcuts import resolve_url
from .models import Usuario

class TesteLoginLogout(TestCase):

    def setUp(self):
        self.senha = "senha"
        self.usuario = Usuario(username="usuario_logado")
        self.usuario.set_password(self.senha)
        self.usuario.save()

        self.url_login = resolve_url(settings.LOGIN_URL)
        self.url_dashboard = resolve_url(settings.LOGIN_REDIRECT_URL)
        self.url_logout = resolve_url("contas:logout")
        self.url_pos_logout = resolve_url(settings.LOGOUT_REDIRECT_URL)

    def test_dashboard_sem_login_redireciona_para_login(self):
        response = self.client.get(self.url_dashboard)
        self.assertRedirects(response, f"{self.url_login}?next={self.url_dashboard}")

    def test_login_valido_redireciona_para_dashboard(self):
        login_response = self.client.post(
            self.url_login,
            {"username": self.usuario.username, "password": self.senha},
        )
        self.assertRedirects(login_response, self.url_dashboard)
        
    def test_logout_redireciona_para_login(self):
        self.client.force_login(self.usuario)
        logout_response = self.client.post(self.url_logout)
        self.assertRedirects(logout_response, self.url_pos_logout)

    def test_logout_desloga_usuario(self):
        self.client.force_login(self.usuario)
        self.client.post(self.url_logout)

        response = self.client.get(self.url_dashboard)
        self.assertRedirects(response, f"{self.url_login}?next={self.url_dashboard}")