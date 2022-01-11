from django.shortcuts import render
from .models import TaskModel


# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def task_view(request):
    tasks = TaskModel.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})
