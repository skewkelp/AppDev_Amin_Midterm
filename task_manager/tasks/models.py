from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, default='Pending')