from django.apps import AppConfig


class AppDbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_db'

def ready(self):
    import app_db.signals
