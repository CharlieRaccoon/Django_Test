from rest_framework import viewsets
from django.shortcuts import render, redirect
from .forms import LessonForm
from django.views.generic import DetailView
from django.core.paginator import Paginator


#Импорт моделей и сериализаторов
from .models import Lesson, Teacher
from .serializers import LessonSerializer, TeacherSerializer

#Создаем новый класс с новой БД для учителей
class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

#Создаем новый класс с новой БД для уроков
class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

#Функция для вывода БД на сайте
def lessons_list(request):
    lessons = Lesson.objects.all()
    paginator = Paginator(lessons, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lessons/lessons_list.html', {'page_obj': page_obj})

def create(request):
    error = ''
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lessons_list')
        else:
            error = 'Форма неверно заполнена'


    form = LessonForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'lessons/create.html', data)

class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lessons/detail_view.html'
    context_object_name = 'lesson'

def teachers_list(request):
    teachers = Teacher.objects.all()
    paginator = Paginator(teachers, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lessons/teachers_list.html', {'page_obj': page_obj})

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'lessons/teacher_detail_view.html'
    context_object_name = 'teacher'