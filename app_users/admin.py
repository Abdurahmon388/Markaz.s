# app_users/admin.py
from django.contrib import admin
from .models import Student, Parents, Worker, Staff

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_line', 'created', 'updated']  # MAYDONLAR STUDENT MODELDA BO‘LISHI KERAK!


class ParentsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'student')
    search_fields = ('student__user__username', 'student__user__phone')

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'salary', 'created')
    search_fields = ('user__username', 'position')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'created')
    search_fields = ('user__username', 'department')

admin.site.register(Parents, ParentsAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Staff, StaffAdmin)


# Register your models here.
