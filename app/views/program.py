from django.shortcuts import render
from django.urls import reverse
from django.forms.models import model_to_dict
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from app.models import Program, Subject
from app.forms import ProgramForm
from app.mixins import ContextMixin
from app.const import CREATE_TEMPLATE, UPDATE_TEMPLATE, DELETE_TEMPLATE

MODEL = Program
FORM = ProgramForm

# Create your views here.


class ProgramList(ContextMixin, ListView):
    template_name = "program_list.html"
    model = MODEL
    queryset = Program.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context.get('current_teacher') and context.get('system_role') != 'vice_principal':
            try:
                subjects = Subject.objects.filter(teacher=context.get('current_teacher'))
                context['object_list'] = self.queryset.filter(plan__subject__in=subjects)
            except Subject.DoesNotExist:
                context['object_list'] = []
        return context


class ProgramCreate(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('makecopy_from'):
            instance = Program.objects.get(pk=int( self.request.GET.get('makecopy_from') ))
            context['form'] = ProgramForm(initial=model_to_dict(instance))
        return context

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