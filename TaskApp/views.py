from django.shortcuts import render
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
            print(form.cleaned_data)
    else:
        form = TaskForm()
    return render(request, 'addTask.html', {'form': form})
