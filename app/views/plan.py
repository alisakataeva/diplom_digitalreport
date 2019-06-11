from django.shortcuts import render
from django.urls import reverse
from django.forms.models import model_to_dict
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from app.models import Plan
from app.forms import PlanForm
from app.mixins import ContextMixin
from app.const import CREATE_TEMPLATE, UPDATE_TEMPLATE, DELETE_TEMPLATE

MODEL = Plan
FORM = PlanForm

# Create your views here.


class PlanList(ContextMixin, ListView):
    template_name = "plan_list.html"
    model = MODEL


class PlanCreate(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('makecopy_from'):
            instance = Plan.objects.get(pk=int( self.request.GET.get('makecopy_from') ))
            context['form'] = PlanForm(initial=model_to_dict(instance))
        return context

    def get_success_url(self, **kwargs):
        return reverse('plan_list')


class PlanUpdate(ContextMixin, UpdateView):
    template_name = UPDATE_TEMPLATE
    model = MODEL
    form_class = FORM

    def get_success_url(self, **kwargs):
        return reverse('plan_list')


class PlanDelete(ContextMixin, DeleteView):
    template_name = DELETE_TEMPLATE
    model = MODEL

    def get_success_url(self, **kwargs):
        return reverse('plan_list')