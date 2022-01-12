from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm

# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def task_view(request):
    tasks = TaskModel.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})


def add_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                TaskModel.objects.create(**form.cleaned_data)
                return redirect('tasks')
            except:
                form.add_error(None, 'incorrect data')

    else:
        form = TaskForm()
    return render(request, 'addTask.html', {'form': form})
