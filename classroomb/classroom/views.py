from django.shortcuts import render
from .models import Classroom, Student
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ClassroomListSerializer, StudentListSerializer
from django.contrib.auth.models import User


class ClassroomList(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer

    def get_queryset(self):
        queryset = Classroom.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(subject__icontains=query) |
                Q(year__icontains=query) |
                Q(teacher__username__icontains=query)
            ).distinct()
        return queryset


class ClassTeacherList(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        user = User.objects.get(id=teacher_id)
        return user.teach_name.all()


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

    def get_queryset(self):
        classroom_id = self.kwargs['classroom_id']
        students = Classroom.objects.get(id=classroom_id)
        return students.class_name.all()


class StudentSearchList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(date_of_birth__icontains=query) |
                Q(exam_grade__icontains=query) |
                Q(classroom__name__icontains=query)
            ).distinct()
        return queryset
