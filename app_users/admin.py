# app_users/admin.py
from django.contrib import admin
from .models import Worker, Staff, Student

admin.site.register(Worker)
admin.site.register(Staff)
admin.site.register(Student)

# Register your models here.
