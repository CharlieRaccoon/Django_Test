from rest_framework import serializers

from .models import Lesson, Teacher

#Сериализуем учителей
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('__all__')

#Сериализуем уроки
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('__all__')
