from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('', views.index, name='index'),
    path('tareas/', views.tareas, name='tareas'),
    path('nueva_tarea/', views.nueva_tarea, name='nueva_tarea'),
    path('ver_tarea/<slug:slug>', views.ver_tarea, name='ver_tarea'),
    path('editar_tarea/<slug:slug>', views.editar_tarea, name='editar_tarea'),
    path('completar_tarea/<slug:slug>', views.completar_tarea, name='completar_tarea'),
    path('restaurar_tarea/<slug:slug>', views.restaurar_tarea, name='restaurar_tarea'),
    path('eliminar_tarea/<slug:slug>', views.eliminar_tarea, name='eliminar_tarea'),
    path('nuevo_proyecto/', views.ProyectoCreateView.as_view(), name='nuevo_proyecto'),
    path('proyectos/', views.ProyectoListView.as_view(), name='proyectos'),
    path('proyectos/<slug:slug>', views.ProyectoDetailView.as_view(), name='ver_proyecto'),
    path('editar_proyecto/<slug:slug>', views.ProyectoUpdateView.as_view(), name='editar_proyecto'),
    path('eliminar_proyecto/<slug:slug>', views.ProyectoDeleteView.as_view(), name='eliminar_proyecto'),
    path('accounts', include('django.contrib.auth.urls')),
    path('register', views.registro_usuario, name="registro_usuario"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 