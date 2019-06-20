# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError

from gibdd.models import GibddUser


# Create your views here.


class GibddIndexView(TemplateView):
    template_name = 'gibdd/index.html'

    def get(self, request, *args, **kwargs):

        user_id = request.session.get('current_user_id')
        # assert False, user_id
        if user_id:
            try:
                user = GibddUser.objects.get(pk=int( user_id ))
                kwargs['user'] = user
            except GibddUser.DoesNotExist:
                return redirect(reverse('gibdd_logout'))
        else:
            return redirect(reverse('gibdd_logout'))

        return super().get(request, *args, **kwargs)


class GibddLoginView(TemplateView):
    template_name = 'gibdd/login.html'

    def post(self, request, *args, **kwargs):

        login = request.POST.get('login')
        password = request.POST.get('password')

        if login and password:
            try:
                user = GibddUser.objects.get(
                    login=login,
                    password=password,
                )
                request.session['current_user_id'] = user.pk
                return redirect(reverse('gibdd_index'))
            except GibddUser.DoesNotExist:
                kwargs['error'] = "Логин или пароль неправильные!"
        else:
            kwargs['error'] = "Введите логин и пароль!"

        return super().get(request, *args, **kwargs)


def logout(request):
    request.session.flush()
    return redirect(reverse('gibdd_login'))