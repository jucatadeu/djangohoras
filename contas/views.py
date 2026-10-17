from django.contrib.auth import views

class LoginView(views.LoginView):
    template_name = "contas/login.html"

