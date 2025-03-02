
# courses/models.py
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

# Create your models here.
