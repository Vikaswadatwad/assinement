from django.db import models
from ..Application.forms import companies

class BenchType(models.Model):
    name = models.CharField(max_length=100, unique=True)

from django.db import models

class BenchType(models.Model):
    name = models.CharField(max_length=100, unique=True)
