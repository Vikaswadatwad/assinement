from django.urls import path
from . import views

urlpatterns = [
    path('benchtype/', views.benchtype_list, name='benchtype_list'),
    path('resources/<int:type_id>/', views.resource_list, name='resource_list'),
    path('book/<int:resource_id>/', views.book_resource, name='book_resource'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('release/<int:resource_id>/', views.release_resource, name='release_resource'),
]


