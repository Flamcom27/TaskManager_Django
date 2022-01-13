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
            TaskModel.objects.create(**form.cleaned_data)
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'addTask.html', {'form': form})


def delete_task_view(request):
    TaskModel.objects.get(id=request.POST['id']).delete()
    return redirect('tasks')


def edit_task_view(request, pk):
    task = TaskModel.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    context = {'form': form}
    return render(request, 'addTask.html', context)
