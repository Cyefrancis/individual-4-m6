from django.db import models
from usuarios.models import UserProfile

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    PENDING = 'Pendiente'
    IN_PROGRESS = 'En Proceso'
    COMPLETED = 'Completada'

    STATE_CHOICES = [
        (PENDING, 'Pendiente'),
        (IN_PROGRESS, 'En Proceso'),
        (COMPLETED, 'Completada')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    state = models.CharField(
        max_length=20,
        choices=STATE_CHOICES,
        default=PENDING
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_tasks')
    assigned_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='assigned_tasks', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    etiquetas = models.ManyToManyField(Etiqueta, related_name='tareas', blank=True)  # Añadir la relación aquí
    
    def __str__(self):
        return self.title
