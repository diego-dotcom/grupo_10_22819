from django import forms
from django.forms import ValidationError
from to_do.models import Tarea, Proyecto


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'prioridad', 'proyecto']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'max_length': 40}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'max_length': 200}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
        }


class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'max_length': 50}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'max_length': 300}),
        }
        

