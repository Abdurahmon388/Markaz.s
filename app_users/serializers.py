from rest_framework import serializers
from .models import Student, Parents, Worker, Staff
from app_courses.models import Course
from app_auth.models import CustomUser
from django.contrib.auth.models import Group


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

from rest_framework import serializers
from app_users.models import Student  # Modelni to‘g‘ri import qiling
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user', 'is_line', 'created', 'updated']  # `name` ni olib tashlang

class ParentsSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Parents
        fields = ['student', 'full_name', 'phone_number', 'address', 'descriptions', 'created', 'updated']


class WorkerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    courses = CourseSerializer(many=True)

    class Meta:
        model = Worker
        fields = ['user', 'position', 'salary', 'courses', 'created']


class StaffSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Staff
        fields = ['user', 'department', 'created']
