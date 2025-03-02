
# app_users/urls.py
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import (
    WorkerListCreateView, WorkerDetailView, WorkerViewSet,
    StudentListCreateView, StudentDetailView, StudentViewSet,
    StaffListCreateView, StaffDetailView, StaffViewSet,
    ParentsListCreateView, ParentsDetailView, ParentsViewSet
)


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'parents', ParentsViewSet)
router.register(r'workers', WorkerViewSet)
router.register(r'staff', StaffViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('workers/', WorkerListCreateView.as_view(), name='worker-list-create'),
    path('workers/<int:pk>/', WorkerDetailView.as_view(), name='worker-detail'),
    
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    
    path('staff/', StaffListCreateView.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    
    path('parents/', ParentsListCreateView.as_view(), name='parents-list-create'),
    path('parents/<int:pk>/', ParentsDetailView.as_view(), name='parents-detail'),
    
    # JWT autentifikatsiya
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

