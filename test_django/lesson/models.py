from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Создаем модель учителя с необходимыми нам формами
class Teacher(models.Model):
    name = models.CharField('ФИО Учителя', max_length=100) # Имя учителя с максимальной длинной в 100 символов
    salary = models.FloatField('Зарплата') # Зарплата учителя с учетом копеек
    date_employment = models.DateField('Дата трудоустройства') # Дата трудоустройства
    avatar = models.ImageField('Фотография', upload_to='images') # Загрузка фотографии с указанием пути сохранения

    # Возвращаяем название именем учителя
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

# Создаем модель уроков
class Lesson(models.Model):
    lesson_name = models.CharField('Название урока', max_length=100) # Название урока с максимальной длинной в 100 символов
    description = models.TextField('Описание') # Описание урока
    # Создаем поле оценки с минимальным и максимальным значением
    assessment = models.PositiveIntegerField('Максимальная оценка', validators=[MinValueValidator(1), MaxValueValidator(10)])
    # Присваиваем уроку учителя
    teacher = models.ForeignKey('Teacher', related_name='lessons', on_delete=models.CASCADE)

    # Возвращаем названия названием урока
    def __str__(self):
        return self.lesson_name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
