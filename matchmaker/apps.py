from django.apps import AppConfig


class MatchmakerConfig(AppConfig):
    name = 'matchmaker'

    def ready(self):
    	from . import signals