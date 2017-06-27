from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = '{{ cookiecutter.initial_app_slug }}'
