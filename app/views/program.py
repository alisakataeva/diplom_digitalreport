from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from app.models import Program
from app.forms import ProgramForm
from app.mixins import ContextMixin
from app.const import CREATE_TEMPLATE, UPDATE_TEMPLATE, DELETE_TEMPLATE

MODEL = Program
FORM = ProgramForm

# Create your views here.


class ProgramList(ContextMixin, ListView):
    template_name = "program_list.html"
    model = MODEL


class ProgramCreate(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_success_url(self, **kwargs):
        return reverse('program_list')


class ProgramUpdate(ContextMixin, UpdateView):
    template_name = UPDATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_success_url(self, **kwargs):
        return reverse('program_list')


class ProgramDelete(ContextMixin, DeleteView):
    template_name = DELETE_TEMPLATE
    model = MODEL

    def get_success_url(self, **kwargs):
        return reverse('program_list')