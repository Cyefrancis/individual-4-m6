from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tarea, Category
from .forms import TareaForm

# Create your views here.
def task_list(request):
    tasks = Tarea.objects.all()
    return render(request, 'task_list.html/',{'task': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Tarea, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

@login_required
def tarea_create_edit(request, tarea_id=None):
    tarea_instance = None

    if tarea_id:
        tarea_instance = get_object_or_404(Tarea, id=tarea_id, user=request.user.profile)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea_instance)
        if form.is_valid():
            tarea = form.save(commit=False)
            assigned_user = form.cleaned_data.get('assigned_user')
            
            if assigned_user:
                tarea.assigned_user = assigned_user
            else:
                # Asignar el usuario actual si no se selecciona ninguno
                tarea.assigned_user = request.user.profile
            
            # Asignar el usuario que creó la tarea
            if not tarea_instance:  # Solo asignar al crear una nueva tarea
                tarea.user = request.user.profile
            
            tarea.save()
            form.save_m2m()  # Guardar relaciones many-to-many
            return redirect('task_detail', task_id=tarea.id)
    else:
        form = TareaForm(instance=tarea_instance)
    
    context = {
        'form': form,
        'title': 'Editar Tarea' if tarea_id else 'Nueva Tarea'
    }
    return render(request, 'task_form.html', context)

def tareas_pendientes_list(request):
    form = TareaForm(request.GET or None)  # Usar los datos GET para inicializar el formulario

    # Obtener todas las tareas
    tareas = Tarea.objects.all()

    if form.is_valid():
        # Aplicar filtros si el formulario es válido y los campos de filtro no están vacíos
        title_contains = form.cleaned_data.get('title_contains')
        if title_contains:
            tareas = tareas.filter(title__icontains=title_contains)

        state = form.cleaned_data.get('state')
        if state:
            tareas = tareas.filter(state=state)

        category = form.cleaned_data.get('category')
        if category:
            tareas = tareas.filter(category=category)

        deadline_before = form.cleaned_data.get('deadline_before')
        if deadline_before:
            tareas = tareas.filter(deadline__lte=deadline_before)

    context = {
        'form': form,
        'tareas': tareas,
    }
    return render(request, 'tareas_pendientes_list.html', context)



def task_edit(request, task_id):
    task = get_object_or_404(Tarea, id=task_id, user=request.user.profile)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_edit', task_id=task.id)
    else:
        form = TareaForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'task': task})



def task_delete(request, task_id):
    task = get_object_or_404(Tarea, id=task_id, user=request.user.profile)
    if request.method == 'POST':
        task.delete()
        return redirect('tareas_pendientes_list')
    return render(request, 'task_confirm_delete.html', {'task': task})