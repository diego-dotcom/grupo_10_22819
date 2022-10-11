from django.shortcuts import render

# Create your views here.

#tareas = []
tareas = [
        {
            'id': 1,
            'titulo': 'Rutas',
            'descripcion': 'Hacer al menos 3 rutas distintas',
            'prioridad': 1,
            'completa': False,
        },
        {
            'id': 2,
            'titulo': 'Vistas',
            'descripcion': 'Utilizar al menos una vista parametrizada',
            'prioridad': 2,
            'completa': False,
        },
        {
            'id': 3,
            'titulo': 'Templates herencia',
            'descripcion': 'Debe existir al menos una relación de herencia entre templates',
            'prioridad': 2,
            'completa': True,
        },
        {
            'id': 4,
            'titulo': 'Git',
            'descripcion': 'El proyecto debe encontrarse subido a un repositorio git',
            'prioridad': 4,
            'completa': False,
        },
        {
            'id': 5,
            'titulo': 'Templates static',
            'descripcion': 'Debe existir al menos un template que utilice archivos estáticos (js, css, etc)',
            'prioridad': 3,
            'completa': False,
        },
    ]

def index(request):
    return render(request, 'to_do/index.html', {'tareas': tareas})

def nueva_tarea(request):
    return render(request, 'to_do/nueva_tarea.html', {'tareas': tareas})

def ver_tarea(request, id):
    return render(request, 'to_do/ver_tarea.html', {'tareas': tareas, 'id': id})