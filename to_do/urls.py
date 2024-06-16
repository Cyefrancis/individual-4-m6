from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/new/', views.tarea_create_edit, name='tarea_create'),
    path('tareas-pendientes/', views.tareas_pendientes_list, name='tareas_pendientes_list'),
    path('tasks/delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('tasks/edit/<int:task_id>/', views.task_edit, name='task_edit'),
    path('ver-tarea/<int:tarea_id>/', views.task_detail, name='ver_tarea'),  # Aquí usar 'task_detail' en lugar de 'ver_tarea' si es la misma vista
]
