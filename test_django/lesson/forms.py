from .models import Lesson
from django.forms import ModelForm, TextInput, NumberInput, Textarea, Select, ChoiceField


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ('__all__')

        widgets = {
            'lesson_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название урока'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание урока'
            }),
            'assessment': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Максимальная оценка (От 0-10)'
            }),
            'teacher': Select(attrs={
                'class': 'form-control',
            })
        }