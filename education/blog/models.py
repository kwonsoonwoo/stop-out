from django.db import models
from django.utils import timezone


class School(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)



class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_at = timezone.now()
        self.save()