
# app_users/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import WorkerListCreateView, WorkerDetailView, StaffListCreateView, StaffDetailView, StudentListCreateView, StudentDetailView

urlpatterns = [
    path('workers/', WorkerListCreateView.as_view(), name='worker-list'),
    path('workers/<int:pk>/', WorkerDetailView.as_view(), name='worker-detail'),
    path('staff/', StaffListCreateView.as_view(), name='staff-list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    path('students/', StudentListCreateView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
