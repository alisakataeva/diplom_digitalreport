import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from app.models import ClassbookNote, Klass, Plan, Subject, Program, SchoolYear, Student, Teacher


class ClassbookNoteForm(forms.ModelForm):

    class Meta:
        model = ClassbookNote
        fields = ['teacher', 'student', 'program', 'data_z', 'time_z', 'pris', 'oc', 'prim']
        widgets = {
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
            'program': forms.Select(attrs={'class': 'form-control'}),
            'data_z': forms.TextInput(attrs={'class': 'form-control'}),
            'time_z': forms.TextInput(attrs={'class': 'form-control'}),
            'pris': forms.Select(attrs={'class': 'form-control'}),
            'oc': forms.Select(attrs={'class': 'form-control'}),
            'prim': forms.Select(attrs={'class': 'form-control'}),
        }


class KlassForm(forms.ModelForm):

    class Meta:
        model = Klass
        fields = ['teacher', 'god_z', 'buk']
        widgets = {
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'god_z': forms.NumberInput(attrs={'class': 'form-control'}),
            'buk': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = ['author', 'subject', 'schoolyear', 'n_ob', 'k_ob', 'kol_ch']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'schoolyear': forms.Select(attrs={'class': 'form-control'}),
            'n_ob': forms.TextInput(attrs={'class': 'form-control'}),
            'k_ob': forms.TextInput(attrs={'class': 'form-control'}),
            'kol_ch': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['teacher', 'pred']
        widgets = {
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'pred': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProgramForm(forms.ModelForm):

    class Meta:
        model = Program
        fields = ['author', 'plan', 'tema', 'kol_ch']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'plan': forms.Select(attrs={'class': 'form-control'}),
            'tema': forms.TextInput(attrs={'class': 'form-control'}),
            'kol_ch': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SchoolYearForm(forms.ModelForm):

    class Meta:
        model = SchoolYear
        fields = ['klass', 'nach_g', 'kon_g']
        widgets = {
            'klass': forms.Select(attrs={'class': 'form-control'}),
            'nach_g': forms.TextInput(attrs={'class': 'form-control'}),
            'kon_g': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['klass', 'fio_uch', 'data_r']
        widgets = {
            'klass': forms.Select(attrs={'class': 'form-control'}),
            'fio_uch': forms.TextInput(attrs={'class': 'form-control'}),
            'data_r': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['fio_uchit', 'dol', 'tel', 'mail', 'log', 'par']
        widgets = {
            'fio_uchit': forms.TextInput(attrs={'class': 'form-control'}),
            'dol': forms.Select(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'log': forms.TextInput(attrs={'class': 'form-control'}),
            'par': forms.TextInput(attrs={'class': 'form-control'}),
        }