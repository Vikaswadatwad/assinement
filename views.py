

from django.shortcuts import render, redirect, get_object_or_404
from .models import Resource, BenchType
from .forms import ResourceForm, BenchTypeForm

def benchtype_list(request):
    types = BenchType.objects.all()
    return render(request, 'companies/benchtype_list.html', {'types': types})

def resource_list(request, type_id):
    resources = Resource.objects.filter(type_id=type_id, status='Available')
    return render(request, 'companies/resource_list.html', {'resources': resources})

def book_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    if request.method == 'POST':
        resource.status = 'Booked'
        resource.booked_by = request.user
        resource.booked_date = datetime.date.today()
        resource.save()
        return redirect('my_bookings')
    return render(request, 'companies/book_resource.html', {'resource': resource})

def my_bookings(request):
    bookings = Resource.objects.filter(booked_by=request.user)
    return render(request, 'companies/my_bookings.html', {'bookings': bookings})

def release_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    if request.method == 'POST':
        resource.status = 'Available'
        resource.booked_by = None
        resource.booked_date = None
        resource.save()
        return redirect('my_bookings')
    return render(request, 'companies/release_resource.html', {'resource': resource})

