from datetime import datetime

from django.db import models

ATTENDANCE_OPTIONS = (
    ('ATTEND', 'Присутствовал'),
    ('ABSENT', 'Не присутствовал по неуважительной причине'),
    ('REASONABLE_ABSENT', 'Не присутствовал по уважительной причине'),
    ('WAS_ILL', 'Не присутствовал по болезни'),
)

MARKS = (
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
)

SCHOOL_ROLES = (
    ('TEACHER', 'Учитель'),
    ('VICE_PRINCIPAL', 'Завуч'),
)

SYSTEM_ROLES = (
    ('ADMIN', 'Администратор'),
    ('USER', 'Пользователь'),
)

# Create your models here.


class Teacher(models.Model):
    fio_uchit = models.CharField(verbose_name=u"ФИО учителя: *", max_length=50)
    dol = models.CharField(verbose_name=u"Должность: *", max_length=50, choices=SCHOOL_ROLES)
    tel = models.CharField(verbose_name=u"Телефон: *", max_length=50)
    mail = models.CharField(verbose_name=u"E-mail: *", max_length=50)
    log = models.CharField(verbose_name=u"Логин: *", max_length=50)
    par = models.CharField(verbose_name=u"Пароль: *", max_length=50)
    tip = models.CharField(verbose_name=u"Тип пользователя: *", max_length=50, choices=SYSTEM_ROLES)

    class Meta:
        verbose_name = 'учитель'
        verbose_name_plural = 'учителя'

    def __str__(self):
        return "<Учитель : %s>" % self.display()

    def display(self):
        return self.fio_uchit


class Klass(models.Model):
    teacher = models.ForeignKey(Teacher, verbose_name="Учитель: *", on_delete=models.CASCADE, null=True)

    god_z = models.IntegerField(verbose_name="Год зачисления: *")
    buk = models.CharField(max_length=1, verbose_name="Буква: *")

    class Meta:
        verbose_name = 'класс'
        verbose_name_plural = 'классы'

    def __str__(self):
        return "<Класс : %s>" % self.get_number()

    def get_number(self):
        gap = datetime.today().year-self.god_z
        month = datetime.today().month
        if gap > 11 or (gap == 11 and month > 8):
            return '(закончил школу)'
        elif month < 9:
            return str( gap ) + self.buk
        else:
            return str( gap+1 ) + self.buk

    def get_students_count(self):
        return self.student_set.count()


class SchoolYear(models.Model):
    klass = models.ForeignKey(Klass, verbose_name="Класс: *", on_delete=models.CASCADE)

    nach_g = models.DateField(verbose_name=u"Начало года: *")
    kon_g = models.DateField(verbose_name=u"Конец года: *")

    class Meta:
        verbose_name = 'учебный год'
        verbose_name_plural = 'учебные года'

    def __str__(self):
        return "<Учебный год : %s>" % self.display()

    def display(self):
        return "%s - %s" % ( str( self.nach_g ), str( self.kon_g ) ) 


class Subject(models.Model):
    teacher = models.ForeignKey(Teacher, verbose_name="Учитель: *", on_delete=models.CASCADE)

    pred = models.CharField(verbose_name=u"Предмет: *", max_length=30)

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'

    def __str__(self):
        return "<Предмет : %s>" % self.pred


class Plan(models.Model):
    author = models.ForeignKey(Teacher, verbose_name="Составитель: *", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name="Предмет: *", on_delete=models.CASCADE)
    schoolyear = models.ForeignKey(SchoolYear, verbose_name="Учебный год: *", on_delete=models.CASCADE)

    n_ob = models.DateField(verbose_name=u"Начало обучения: *")
    k_ob = models.DateField(verbose_name=u"Конец обучения: *")
    kol_ch = models.IntegerField(verbose_name=u"Количество часов: *")

    class Meta:
        verbose_name = 'план'
        verbose_name_plural = 'планы'

    def __str__(self):
        return "<План : %s (Кол-во часов: %s, класс: %s, предмет: %s)>" % (
            self.display(), 
            str( self.kol_ch ), 
            self.schoolyear.klass.get_number(),
            self.subject.pred
        )

    def display(self):
        return "%s - %s" % ( str( self.n_ob ), str( self.k_ob ) )


class Program(models.Model):
    author = models.ForeignKey(Teacher, verbose_name="Составитель: *", on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, verbose_name="План: *", on_delete=models.CASCADE)

    tema = models.CharField(verbose_name=u"Тема урока: *", max_length=100)
    kol_ch = models.IntegerField(verbose_name=u"Количество часов: *")

    class Meta:
        verbose_name = 'программа'
        verbose_name_plural = 'программы'

    def __str__(self):
        return "<Программа : %s>" % self.tema


class Student(models.Model):
    klass = models.ForeignKey(Klass, verbose_name="Класс: *", on_delete=models.CASCADE)

    fio_uch = models.CharField(verbose_name=u"ФИО ученика: *", max_length=50)
    data_r = models.DateField(verbose_name=u"Дата рождения: *")

    class Meta:
        verbose_name = 'ученик'
        verbose_name_plural = 'ученики'

    def __str__(self):
        return "<Ученик : %s>" % self.display()

    def display(self):
        return self.fio_uch


class ClassbookNote(models.Model):
    teacher = models.ForeignKey(Teacher, verbose_name="Учитель: *", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="Ученик: *", on_delete=models.CASCADE)
    program = models.ForeignKey(Program, verbose_name="Программа: *", on_delete=models.CASCADE)

    data_z = models.DateField(verbose_name="Дата занятия: *")
    time_z = models.TimeField(verbose_name="Время занятия: *")
    pris = models.CharField(max_length=20, verbose_name="Присутствие: *", choices=ATTENDANCE_OPTIONS, default='ATTEND')
    oc = models.CharField(max_length=20, verbose_name="Оценка:", choices=MARKS, blank=True, null=True)
    prim = models.CharField(max_length=250, verbose_name="Примечание:", blank=True, null=True)

    class Meta:
        verbose_name = 'запись в журнале'
        verbose_name_plural = 'записи в журнале'

    def __str__(self):
        return "<Запись в журнале : %s, %s %s>" % ( self.student.fio_uch, str( self.data_z ), str( self.time_z ) )

    def get_subject(self):
        return self.program.plan.subject.pred
