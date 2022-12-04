from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from to_do.models import Tarea, Proyecto
from to_do.forms import TareaForm, ProyectoForm, NuevoUsuarioForm

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib import messages

from django.contrib.auth.decorators import login_required


def index(request):
    tareas = Tarea.objects.all()
    return render(request, 'to_do/index.html', {'tareas': tareas})

@login_required
def tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'to_do/tareas.html', {'tareas': tareas})

@login_required
def nueva_tarea(request):
    if(request.method=='POST'):
        formulario = TareaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tareas')
    else:
        formulario = TareaForm()
    return render(request,'to_do/nueva_tarea.html', {'formulario': formulario})
    

def ver_tarea(request, slug):
    tareas = Tarea.objects.all()
    return render(request, 'to_do/ver_tarea.html', {'tareas': tareas, 'slug': slug})


def editar_tarea(request, slug):
    try:
        tarea = Tarea.objects.get(slug=slug)
    except Tarea.DoesNotExist:
        return render(request,'to_do/index.html')

    if(request.method=='POST'):
        formulario = TareaForm(request.POST,instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return redirect('tareas')
    else:
        formulario = TareaForm(instance=tarea)
    return render(request,'to_do/editar_tarea.html',{'formulario': formulario})


def completar_tarea(request, slug):
    try:
        tarea = Tarea.objects.get(slug=slug)
    except Tarea.DoesNotExist:
        return render(request,'to_do/index.html')
    tarea.complete()
    return redirect('tareas')


def restaurar_tarea(request, slug):
    try:
        tarea = Tarea.objects.get(slug=slug)
    except Tarea.DoesNotExist:
        return render(request,'to_do/index.html')
    tarea.restore()
    return redirect('tareas')


def eliminar_tarea(request, slug):
    try:
        tarea = Tarea.objects.get(slug=slug)
    except Tarea.DoesNotExist:
        return render(request,'to_do/index.html')
    tarea.delete()
    return redirect('tareas')


class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name_suffix = '_create_form'
    success_url ="/proyectos/"


class ProyectoListView(ListView):
    model = Proyecto
    context_object_name = 'proyectos'
    template_name = 'to_do/proyectos.html'
    queryset = Proyecto.objects.all()
    ordering = ['nombre']
    

class ProyectoDetailView(DetailView):
    model = Proyecto
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProyectoUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name_suffix = '_update_form'
    success_url ="/proyectos/"


class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyectos')



def registro_usuario(request):
	if request.method == "POST":
		form = NuevoUsuarioForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NuevoUsuarioForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})


