from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nueva_tarea/', views.nueva_tarea, name='nueva_tarea'),
    path('ver_tarea/<int:id>', views.ver_tarea, name='ver_tarea'),
]