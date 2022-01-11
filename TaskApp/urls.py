from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('tasks', views.task_view)
]