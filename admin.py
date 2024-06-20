from django.contrib import admin
from .models import User, Company, BenchType, Resource, Booking

admin.site.register(User)
admin.site.register(Company)
admin.site.register(BenchType)
admin.site.register(Resource)
admin.site.register(Booking)

