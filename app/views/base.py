from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from app.mixins import ContextMixin

from app.models import Teacher

# Create your views here.


class IndexView(ContextMixin, TemplateView):
    template_name = "index.html"


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.method == 'POST':

            login = self.request.POST.get('login')
            password = self.request.POST.get('password')

            if not login or not password:
                ctx['error'] = 'Введите логин и пароль.'
            else:
                try:
                    teacher = Teacher.objects.get(log=login, par=password)
                except Teacher.DoesNotExist:
                    ctx['error'] = 'Логин и пароль не верны.'
            
        return ctx

    def post(self, request, *args, **kwargs):

        login = request.POST.get('login')
        password = request.POST.get('password')
        if login and password:
            try:
                teacher = Teacher.objects.get(log=login, par=password)
                request.session['current_teacher_id'] = teacher.pk
                return redirect('/')
            except Teacher.DoesNotExist:
                pass

        return super().get(request, *args, **kwargs)


class SignupView(TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.method == 'POST':

            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            email = self.request.POST.get('email')
            login = self.request.POST.get('login')
            password = self.request.POST.get('password')

            if not name or not phone or not email or not login or not password:
                ctx['error'] = 'Введите все данные.'
            
        return ctx

    def post(self, request, *args, **kwargs):

        name = self.request.POST.get('name')
        role = self.request.POST.get('role')
        phone = self.request.POST.get('phone')
        email = self.request.POST.get('email')
        login = self.request.POST.get('login')
        password = self.request.POST.get('password')
        system_role = self.request.POST.get('system_role')

        if name and phone and email and login and password:
            teacher = Teacher.objects.create(
                fio_uchit=name,
                dol=role,
                tel=phone,
                mail=email,
                log=login,
                par=password,
                tip=system_role
            )
            request.session['current_teacher_id'] = teacher.pk
            return redirect('/')

        return super().get(request, *args, **kwargs)


def logout(request):
    request.session.flush()
    return redirect('/')