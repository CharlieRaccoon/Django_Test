from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views
from .views import LessonViewSet, TeacherViewSet
# Указание url через библиотеку rest_framework для автоматической маршрутизации
router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='id')
router.register(r'teachers', TeacherViewSet, basename='id')

urlpatterns = [
    path('lesson/', views.lessons_list, name='lessons_list'),
    path('create/', views.create, name='create'),
    path('lesson/<int:pk>', views.LessonDetailView.as_view(), name='lesson-detail'),
    path('teacher/', views.teachers_list, name='teachers_list'),
    path('teacher/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
] + router.urls
