from django.apps import AppConfig
from .models import Profile


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
