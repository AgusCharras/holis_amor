from django.apps import AppConfig


class CalendarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'holis.calendario'
    
    def ready(self):
        import holis.calendario.signals
