from django.shortcuts import render, redirect
from .models import BenchType
from ..Application.forms import companies

def benchtype_list(request):
    types = BenchType.objects.all()
    return render(request, 'admin/benchtype_list.html', {'types': types})

def benchtype_add(request):
    if request.method == 'POST':
        form = companies(request.POST)
        if form.is_valid():
            form.save()
            return redirect('benchtype_list')
    else:
        form = companies()
    return render(request, 'admin/benchtype_form.html', {'form': form})

def benchtype_edit(request, pk):
    type = BenchType.objects.get(pk=pk)
    if request.method == 'POST':
        form = companies(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('benchtype_list')
    else:
        form = companies(instance=type)
    return render(request, 'admin/benchtype_form.html', {'form': form})

def benchtype_delete(request, pk):
    type = BenchType.objects.get(pk=pk)
    type.delete()
    return redirect('benchtype_list')
  
def resource_list(request, bench_type_id):
    resources = Resource.objects.filter(bench_type_id=bench_type_id, booked_by__isnull=True)
    return render(request, 'company/resource_list.html', {'resources': resources})



