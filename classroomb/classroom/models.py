from django.db import models
from django.contrib.auth.models import User


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    year = models.IntegerField()
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='teach_name')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    # CHOICES = Choices('male', 'female')
   # gender_choices = models.CharField(
    #    choices = CHOICES, default = CHOICES.draft, max_length = 6)
    exam_grade = models.DecimalField(max_digits=3, decimal_places=2)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name='class_name')

    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
