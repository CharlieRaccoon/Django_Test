from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    salary = models.FloatField()
    date_employment = models.DateField()


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=255)
    description = models.TextField()
    assessment = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    teacher = models.ForeignKey('Teacher', related_name='lessons', on_delete=models.CASCADE)