from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/new/', views.task_create, name='task_create'),
    path('tareas-pendientes/', views.tareas_pendientes_list, name='tareas_pendientes_list'),
    path('ver-tarea/<int:tarea_id>/', views.ver_tarea, name='ver_tarea'),
]
