import datetime

from django.db import models

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.heading
    heading=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    date=models.DateField(default=datetime.date.today)
    blog=models.TextField(blank=True)

