from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea, Category

from .forms import TareaForm

# Create your views here.
def task_list(request):
    tasks = Tarea.objects.all()
    return render(request, 'todo/task_list.html',{'task': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Tarea, pk=task_id)
    return render(request, 'todo/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TareaForm()
    return render(request, 'todo/task_form.html', {'form': form})








