# Generated by Django 2.1 on 2019-06-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_klass_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='tema',
            field=models.CharField(max_length=100, verbose_name='Тема урока: *'),
        ),
    ]
