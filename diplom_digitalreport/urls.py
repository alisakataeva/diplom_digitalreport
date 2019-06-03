"""diplom_digitalreport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view(), name='index'),

    path('classbooknotes', views.ClassbookNoteList.as_view(), name='classbooknote_list'),
    path('classbooknotes/create', views.ClassbookNoteCreate.as_view(), name='classbooknote_create'),
    path('classbooknotes/<int:pk>/update', views.ClassbookNoteUpdate.as_view(), name='classbooknote_update'),
    path('classbooknotes/<int:pk>/delete', views.ClassbookNoteDelete.as_view(), name='classbooknote_delete'),

    path('klasses', views.KlassList.as_view(), name='klass_list'),
    path('klasses/create', views.KlassCreate.as_view(), name='klass_create'),
    path('klasses/<int:pk>/update', views.KlassUpdate.as_view(), name='klass_update'),
    path('klasses/<int:pk>/delete', views.KlassDelete.as_view(), name='klass_delete'),

    path('plans', views.PlanList.as_view(), name='plan_list'),
    path('plans/create', views.PlanCreate.as_view(), name='plan_create'),
    path('plans/<int:pk>/update', views.PlanUpdate.as_view(), name='plan_update'),
    path('plans/<int:pk>/delete', views.PlanDelete.as_view(), name='plan_delete'),

    path('subjects', views.SubjectList.as_view(), name='subject_list'),
    path('subjects/create', views.SubjectCreate.as_view(), name='subject_create'),
    path('subjects/<int:pk>/update', views.SubjectUpdate.as_view(), name='subject_update'),
    path('subjects/<int:pk>/delete', views.SubjectDelete.as_view(), name='subject_delete'),

    path('programs', views.ProgramList.as_view(), name='program_list'),
    path('programs/create', views.ProgramCreate.as_view(), name='program_create'),
    path('programs/<int:pk>/update', views.ProgramUpdate.as_view(), name='program_update'),
    path('programs/<int:pk>/delete', views.ProgramDelete.as_view(), name='program_delete'),

    path('schoolyears', views.SchoolYearList.as_view(), name='schoolyear_list'),
    path('schoolyears/create', views.SchoolYearCreate.as_view(), name='schoolyear_create'),
    path('schoolyears/<int:pk>/update', views.SchoolYearUpdate.as_view(), name='schoolyear_update'),
    path('schoolyears/<int:pk>/delete', views.SchoolYearDelete.as_view(), name='schoolyear_delete'),

    path('students', views.StudentList.as_view(), name='student_list'),
    path('students/create', views.StudentCreate.as_view(), name='student_create'),
    path('students/<int:pk>/update', views.StudentUpdate.as_view(), name='student_update'),
    path('students/<int:pk>/delete', views.StudentDelete.as_view(), name='student_delete'),

    path('teachers', views.TeacherList.as_view(), name='teacher_list'),
    path('teachers/create', views.TeacherCreate.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update', views.TeacherUpdate.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete', views.TeacherDelete.as_view(), name='teacher_delete'),

    path('reports/study_results', views.StudyResultsReportView.as_view(), name='report_study_results'),
    path('reports/study_level', views.StudyLevelReportView.as_view(), name='report_study_level'),
    path('reports/klass_study_level', views.KlassStudyLevelReportView.as_view(), name='report_klass_study_level'),
    path('reports/klass_attendance', views.KlassAttendanceReportView.as_view(), name='report_klass_attendance'),
    path('reports/total_study_results', views.TotalStudyResultsReportView.as_view(), name='report_total_study_results'),
    path('reports/total_study_level', views.TotalStudyLevelReportView.as_view(), name='report_total_study_level'),
    path('reports/total_attendance', views.TotalAttendanceReportView.as_view(), name='report_total_attendance'),
]