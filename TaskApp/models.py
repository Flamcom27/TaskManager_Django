from django.db import models


# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=30, verbose_name="Task", editable=True)
    description = models.CharField(max_length=250, null=True, blank=True, editable=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False, editable=True)

    def __repr__(self):
        return self.title
