from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Worker, Student, Staff, Parents
from .serializers import WorkerSerializer, StudentSerializer, StaffSerializer, ParentsSerializer


# **ViewSet API Views**
class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ParentsViewSet(viewsets.ModelViewSet):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


# **Function-based API View**
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


# **Generic-based CRUD API Views**
class WorkerListCreateView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StaffListCreateView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class ParentsListCreateView(generics.ListCreateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer


class ParentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer
