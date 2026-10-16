from django.core.management.commands import shell

class Command(shell.Command):
    def get_auto_imports(self):
        import horas.atalhos
        
        return super().get_auto_imports() + [
            "django.db.models.Sum",
            "django.contrib.auth.get_user_model",
            "horas.atalhos",
        ]