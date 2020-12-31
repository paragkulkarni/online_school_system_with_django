from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, FormView
from .models import Standard, Subject, Lesson
# Create your views here.


class StandardListView(ListView):
    model = Standard
    context_object_name = 'standards'
    template_name='curriculam/standard_list_view.html'


class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name='curriculam/subject_list_view.html'


class LessonListView(DetailView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'curriculam/lesson_list_view.html'


class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = 'lessons'
    template_name='curriculam/lesson_detail_view.html'