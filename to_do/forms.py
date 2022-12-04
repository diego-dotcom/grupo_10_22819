from django import forms
from django.forms import ValidationError
from to_do.models import Tarea, Proyecto

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'prioridad', 'proyecto', 'usuario']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'max_length': 40}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'max_length': 200}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }


class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'max_length': 50}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'max_length': 300}),
        }
        


class NuevoUsuarioForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NuevoUsuarioForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user