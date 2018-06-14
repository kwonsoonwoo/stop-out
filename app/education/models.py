from django.db import models
from django.utils import timezone


class School(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name