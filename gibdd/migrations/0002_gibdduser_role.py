# Generated by Django 2.2.1 on 2019-06-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gibdd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gibdduser',
            name='role',
            field=models.CharField(blank=True, choices=[('HEAD', 'Начальник ОГИБДД'), ('WORKER', 'Сотрудник ДПС')], max_length=20, null=True, verbose_name='Тип пользователя'),
        ),
    ]
