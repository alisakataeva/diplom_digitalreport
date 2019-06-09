from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from app.models import ClassbookNote
from app.forms import ClassbookNoteForm
from app.mixins import ContextMixin
from app.const import CREATE_TEMPLATE, UPDATE_TEMPLATE, DELETE_TEMPLATE

MODEL = ClassbookNote
FORM = ClassbookNoteForm

# Create your views here.


class ClassbookNoteList(ContextMixin, ListView):
    template_name = "classbooknote_list.html"
    model = MODEL
    queryset = ClassbookNote.objects.all().order_by("data_z")


class ClassbookNoteCreate(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_success_url(self, **kwargs):
        return reverse('classbooknote_list')


class ClassbookNoteUpdate(ContextMixin, UpdateView):
    template_name = UPDATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_success_url(self, **kwargs):
        return reverse('classbooknote_list')


class ClassbookNoteDelete(ContextMixin, DeleteView):
    template_name = DELETE_TEMPLATE
    model = MODEL

    def get_success_url(self, **kwargs):
        return reverse('classbooknote_list')