from django.db import models

from django.utils.text import slugify
from django.db.models.signals import pre_save

import uuid

from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    descripcion = models.TextField(max_length=300, verbose_name="Descripción", null=True)
    slug = models.SlugField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.nombre


def set_slug_proyecto(sender, instance, *args, **kwargs):    # callback
    if instance.nombre and not instance.slug:
        slug = slugify(instance.nombre)

        while Proyecto.objects.filter(slug=slug).exists():
            slug = slugify(f"{instance.nombre}-{str(uuid.uuid4)[:8]}")
            
        instance.slug = slug

# Antes de que un objeto Tarea se almacena ejecuta el callback
pre_save.connect(set_slug_proyecto, sender=Proyecto)



class Tarea(models.Model):

    prioridades = [
        (1,'Urgente e importante'),
        (2,'Urgente'),
        (3,'Importante'),
        (4,'Ni urgente ni importante (Delegar)'),
    ]

    titulo = models.CharField(max_length=50, verbose_name="Título")
    descripcion = models.TextField(max_length=200, verbose_name="Descripción", null=True)
    prioridad = models.IntegerField(choices=prioridades, default=1)
    fecha = models.DateField(verbose_name="Fecha", auto_now=True)
    vigente = models.BooleanField(default=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, blank=False, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo

    def complete(self):
        self.vigente=False
        super().save()
    
    def restore(self):
        self.vigente=True
        super().save()



def set_slug_tarea(sender, instance, *args, **kwargs):    # callback
    if instance.titulo and not instance.slug:
        slug = slugify(instance.titulo)

        while Tarea.objects.filter(slug=slug).exists():
            slug = slugify(f"{instance.titulo}-{str(uuid.uuid4)[:8]}")
            
        instance.slug = slug

# Antes de que un objeto Tarea se almacena ejecuta el callbak
pre_save.connect(set_slug_tarea, sender=Tarea)

