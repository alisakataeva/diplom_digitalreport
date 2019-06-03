from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from app.models import Subject
from app.forms import SubjectForm
from app.mixins import ContextMixin
from app.const import CREATE_TEMPLATE, UPDATE_TEMPLATE, DELETE_TEMPLATE

MODEL = Subject
FORM = SubjectForm

# Create your views here.


class SubjectList(ContextMixin, ListView):
    template_name = "subject_list.html"
    model = MODEL


class SubjectCreate(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_success_url(self, **kwargs):
        return reverse('subject_list')


class SubjectUpdate(ContextMixin, UpdateView):
    template_name = UPDATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_success_url(self, **kwargs):
        return reverse('subject_list')


class SubjectDelete(ContextMixin, DeleteView):
    template_name = DELETE_TEMPLATE
    model = MODEL

    def get_success_url(self, **kwargs):
        return reverse('subject_list')