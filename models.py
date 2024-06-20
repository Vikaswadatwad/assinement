
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('company', 'Company'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

class BenchType(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    available_from = models.DateField()
    bench_type = models.ForeignKey(BenchType, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)

class Booking(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    released_at = models.DateTimeField(null=True, blank=True)
