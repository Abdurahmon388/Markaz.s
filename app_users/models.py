from django.db import models
from app_auth.models import CustomUser
from app_courses.models import Course, Group


class Student(models.Model):
    name = models.CharField(max_length=255)  # Yangi maydon qo‘shish
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  
    is_line = models.BooleanField(default=False)  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  



class Parents(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name if self.full_name else "No Name"


class Worker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="worker_profile")
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    courses = models.ManyToManyField(Course, related_name="workers")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.position}"


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="staff_profile")
    department = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.department}"
