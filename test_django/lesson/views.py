from rest_framework import viewsets
from django.shortcuts import render, redirect
from .forms import LessonForm
from django.views.generic import DetailView
from rest_framework.pagination import PageNumberPagination


# Импорт моделей и сериализаторов
from .models import Lesson, Teacher
from .serializers import LessonSerializer, TeacherSerializer

# Пагинация
class PagePagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = page_size
    max_page_size = 10


# Создаем новый класс с новой БД для учителей
class TeacherViewSet(viewsets.ModelViewSet):
    """Вывод списка учителей"""
    serializer_class = TeacherSerializer
    pagination_class = PagePagination
    queryset = Teacher.objects.all()

# Создаем новый класс с новой БД для уроков
class LessonViewSet(viewsets.ModelViewSet):
    """Вывод списка уроков"""
    serializer_class = LessonSerializer
    pagination_class = PagePagination
    queryset = Lesson.objects.all()

# Функция для вывода БД на сайте
def lessons_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lessons_list.html', {'lessons': lessons})

# Функция для создания урока
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
    return render(request, 'lessons/teachers_list.html', {'teachers': teachers})

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'lessons/teacher_detail_view.html'
    context_object_name = 'teacher'