# Generated by Django 2.2.1 on 2019-06-04 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('god_z', models.IntegerField(verbose_name='Год зачисления')),
                ('buk', models.CharField(max_length=1, verbose_name='буква')),
            ],
            options={
                'verbose_name': 'класс',
                'verbose_name_plural': 'классы',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_ob', models.DateField(verbose_name='Начало обучения')),
                ('k_ob', models.DateField(verbose_name='Конец обучения')),
                ('kol_ch', models.IntegerField(verbose_name='Количество часов')),
            ],
            options={
                'verbose_name': 'план',
                'verbose_name_plural': 'планы',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_uchit', models.CharField(max_length=50, verbose_name='ФИО учителя')),
                ('dol', models.CharField(choices=[('TEACHER', 'Учитель'), ('VICE_PRINCIPAL', 'Завуч')], max_length=50, verbose_name='Должность')),
                ('tel', models.CharField(max_length=50, verbose_name='Телефон')),
                ('mail', models.CharField(max_length=50, verbose_name='E-mail')),
                ('log', models.CharField(max_length=50, verbose_name='Логин')),
                ('par', models.CharField(max_length=50, verbose_name='Пароль')),
                ('tip', models.CharField(choices=[('ADMIN', 'Администратор'), ('USER', 'Пользователь')], max_length=50, verbose_name='Тип пользователя')),
            ],
            options={
                'verbose_name': 'учитель',
                'verbose_name_plural': 'учителя',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pred', models.CharField(max_length=30, verbose_name='Предмет')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teacher', verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'предмет',
                'verbose_name_plural': 'предметы',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_uch', models.CharField(max_length=50, verbose_name='ФИО ученика')),
                ('data_r', models.DateField(verbose_name='Дата рождения')),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Klass', verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'ученик',
                'verbose_name_plural': 'ученики',
            },
        ),
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nach_g', models.DateField(verbose_name='Начало года')),
                ('kon_g', models.DateField(verbose_name='Конец года')),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Klass', verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'учебный год',
                'verbose_name_plural': 'учебные года',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=30, verbose_name='Тема урока')),
                ('kol_ch', models.IntegerField(verbose_name='Количество часов')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teacher', verbose_name='Составитель')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Plan', verbose_name='План')),
            ],
            options={
                'verbose_name': 'программа',
                'verbose_name_plural': 'программы',
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teacher', verbose_name='Составитель'),
        ),
        migrations.AddField(
            model_name='plan',
            name='schoolyear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SchoolYear', verbose_name='Учебный год'),
        ),
        migrations.AddField(
            model_name='plan',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Subject', verbose_name='Предмет'),
        ),
        migrations.CreateModel(
            name='ClassbookNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_z', models.DateField(verbose_name='Дата занятия')),
                ('time_z', models.TimeField(verbose_name='Время занятия')),
                ('pris', models.CharField(choices=[('ATTEND', 'Присутствовал'), ('ABSENT', 'Не присутствовал по неуважительной причине'), ('REASONABLE_ABSENT', 'Не присутствовал по уважительной причине'), ('WAS_ILL', 'Не присутствовал по болезни')], default='ATTEND', max_length=20, verbose_name='Присутствие')),
                ('oc', models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2')], max_length=20, verbose_name='Оценка')),
                ('prim', models.CharField(max_length=250, verbose_name='Примечание')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Program', verbose_name='Программа')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student', verbose_name='Ученик')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teacher', verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'запись в журнале',
                'verbose_name_plural': 'записи в журнале',
            },
        ),
    ]
