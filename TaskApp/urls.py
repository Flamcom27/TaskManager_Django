from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('tasks', views.task_view, name='tasks'),
    path('add_task', views.add_task_view, name='add_task'),
    path('delete_task', views.delete_task_view, name='delete_task')
]