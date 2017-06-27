from django.db import models


class {{ cookiecutter.initial_model_name }}(models.Model):
    name = models.CharField(max_length=100)
