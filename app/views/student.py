from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from app.models import Student
from app.forms import StudentForm
from app.mixins import ContextMixin
from app.const import CREATE_TEMPLATE, UPDATE_TEMPLATE, DELETE_TEMPLATE

MODEL = Student
FORM = StudentForm

# Create your views here.


class StudentList(ContextMixin, ListView):
    template_name = "student_list.html"
    model = MODEL


class StudentCreate(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_success_url(self, **kwargs):
        return reverse('student_list')


class StudentUpdate(ContextMixin, UpdateView):
    template_name = UPDATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_success_url(self, **kwargs):
        return reverse('student_list')


class StudentDelete(ContextMixin, DeleteView):
    template_name = DELETE_TEMPLATE
    model = MODEL

    def get_success_url(self, **kwargs):
        return reverse('student_list')