from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'hc.accounts'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import hc.accounts.signals  # Import the signals
