
# app_users/models.py
from django.db import models
from app_courses.models import Course
from app_auth.models import CustomUser  # TO‘G‘RI IMPORT

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

    def __str__(self):
        return f"{self.user.username} - {self.department}"

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="student_profile")
    grade = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course, related_name="students")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.grade}"