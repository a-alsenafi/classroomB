from rest_framework import serializers
from .models import Classroom, Student


class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'name', 'subject',
                  'year']


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'date_of_birth',
                  'exam_grade', 'classroom', 'img']
