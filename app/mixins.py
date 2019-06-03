from django.contrib.auth.models import User
from django.urls import resolve


class ContextMixin:

    def get_context_data(self, **kwargs):

        if self.request.GET.get('next'):
            kwargs['next'] = self.request.GET.get('next')

        return super(ContextMixin, self).get_context_data(**kwargs)