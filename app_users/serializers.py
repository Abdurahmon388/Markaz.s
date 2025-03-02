
# app_users/serializers.py
from rest_framework import serializers
from app_auth.models import CustomUser
from .models import Worker, Staff, Student

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_worker', 'is_staff', 'is_student', 'is_admin', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class WorkerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Worker
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data, is_worker=True)
        return Worker.objects.create(user=user, **validated_data)

class StaffSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Staff
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data, is_staff=True)
        return Staff.objects.create(user=user, **validated_data)

class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data, is_student=True)
        return Student.objects.create(user=user, **validated_data)

