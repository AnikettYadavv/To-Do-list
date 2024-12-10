from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# List tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/tasklist.html', {'tasks': tasks})

# Add new task
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/addtask.html', {'form': form})