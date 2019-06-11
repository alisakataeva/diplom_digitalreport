from django.contrib.auth.models import User
from django.urls import resolve

from app.models import Teacher, Klass


class ContextMixin:

    def get_context_data(self, **kwargs):

        if self.request.GET.get('next'):
            kwargs['next'] = self.request.GET.get('next')

        kwargs['current_teacher'] = None
        kwargs['current_klass'] = None

        if self.request.session.get("current_teacher_id"):

            try:
                kwargs['current_teacher'] = Teacher.objects.get(pk=int( self.request.session.get("current_teacher_id") ))
            except Teacher.DoesNotExist:
                pass

            if kwargs['current_teacher']:
                try:
                    kwargs['current_klass'] = Klass.objects.get(teacher=kwargs['current_teacher'])
                except Klass.DoesNotExist:
                    pass

        # assert False, kwargs['current_teacher']

        return super(ContextMixin, self).get_context_data(**kwargs)