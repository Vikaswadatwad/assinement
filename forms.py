from django import forms
from .models import Resource, BenchType

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'type', 'description', 'available_from']

class companies(forms.ModelForm):
    class Meta:
        model = BenchType
        fields = ['name']

