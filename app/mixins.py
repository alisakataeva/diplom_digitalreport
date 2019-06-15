from django.contrib.auth.models import User
from django.urls import resolve

from app.models import Teacher, Klass


class ContextMixin:

    def get_context_data(self, **kwargs):

        if self.request.GET.get('next'):
            kwargs['next'] = self.request.GET.get('next')

        kwargs['current_teacher'] = None
        kwargs['current_klass'] = None
        kwargs['system_role'] = None

        if self.request.session.get("current_teacher_id"):

            try:
                user = Teacher.objects.get(pk=int( self.request.session.get("current_teacher_id") ))
            except Teacher.DoesNotExist:
                pass

            if user:
                kwargs['current_teacher'] = user
                if user.dol == 'TEACHER':
                    kwargs['system_role'] = 'teacher'
                elif user.dol == 'VICE_PRINCIPAL':
                    kwargs['system_role'] = 'vice_principal'
                try:
                    kwargs['current_klass'] = Klass.objects.get(teacher=user)
                except Klass.DoesNotExist:
                    pass

        kwargs['current_teacher'] = user

        return super(ContextMixin, self).get_context_data(**kwargs)