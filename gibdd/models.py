from django.db import models

# Create your models here.


class GibddUser(models.Model):
    name = models.CharField(max_length=30, verbose_name="ФИО")
    login = models.CharField(max_length=20, verbose_name="Логин")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    role = models.CharField(max_length=20, verbose_name="Тип пользователя",\
        choices=(('HEAD', 'Начальник ОГИБДД'), ('WORKER', 'Сотрудник ДПС')), blank=True, null=True)

    class Meta:
        verbose_name = "пользователь гибдд"
        verbose_name_plural = "пользователи гибдд"