from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea, Category

from .forms import TareaForm

# Create your views here.
def task_list(request):
    tasks = Tarea.objects.all()
    return render(request, 'task_list.html/',{'task': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Tarea, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TareaForm()
    return render(request, 'task_form.html', {'form': form})

def tareas_pendientes_list(request):
    user_profile = request.user.profile
    tareas = Tarea.objects.filter(user=user_profile, state='Pendiente').order_by('deadline')

    context = {
        'tareas': tareas
    }
    return render(request, 'tareas_pendientes_list.html/')

def ver_tarea(request, tarea_id):
    tasks = get_object_or_404(Tarea, id=tarea_id)
    
    context = {
        'tasks': tasks
    }
    return render(request, 'ver_tarea.html', context)



