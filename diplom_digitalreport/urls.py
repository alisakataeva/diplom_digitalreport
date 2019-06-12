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
from app.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login_required(views.IndexView.as_view()), name='index'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('logout/', views.logout, name="logout"),

    path('classbooknotes', login_required(views.ClassbookNoteList.as_view()), name='classbooknote_list'),
    path('classbooknotes/create', login_required(views.ClassbookNoteCreate.as_view()), name='classbooknote_create'),
    path('classbooknotes/<int:pk>/update', login_required(views.ClassbookNoteUpdate.as_view()), name='classbooknote_update'),
    path('classbooknotes/<int:pk>/delete', login_required(views.ClassbookNoteDelete.as_view()), name='classbooknote_delete'),

    path('klasses', login_required(views.KlassList.as_view()), name='klass_list'),
    path('klasses/create', login_required(views.KlassCreate.as_view()), name='klass_create'),
    path('klasses/<int:pk>/update', login_required(views.KlassUpdate.as_view()), name='klass_update'),
    path('klasses/<int:pk>/delete', login_required(views.KlassDelete.as_view()), name='klass_delete'),

    path('plans', login_required(views.PlanList.as_view()), name='plan_list'),
    path('plans/create', login_required(views.PlanCreate.as_view()), name='plan_create'),
    path('plans/<int:pk>/update', login_required(views.PlanUpdate.as_view()), name='plan_update'),
    path('plans/<int:pk>/delete', login_required(views.PlanDelete.as_view()), name='plan_delete'),

    path('subjects', login_required(views.SubjectList.as_view()), name='subject_list'),
    path('subjects/create', login_required(views.SubjectCreate.as_view()), name='subject_create'),
    path('subjects/<int:pk>/update', login_required(views.SubjectUpdate.as_view()), name='subject_update'),
    path('subjects/<int:pk>/delete', login_required(views.SubjectDelete.as_view()), name='subject_delete'),

    path('programs', login_required(views.ProgramList.as_view()), name='program_list'),
    path('programs/create', login_required(views.ProgramCreate.as_view()), name='program_create'),
    path('programs/<int:pk>/update', login_required(views.ProgramUpdate.as_view()), name='program_update'),
    path('programs/<int:pk>/delete', login_required(views.ProgramDelete.as_view()), name='program_delete'),

    path('schoolyears', login_required(views.SchoolYearList.as_view()), name='schoolyear_list'),
    path('schoolyears/create', login_required(views.SchoolYearCreate.as_view()), name='schoolyear_create'),
    path('schoolyears/<int:pk>/update', login_required(views.SchoolYearUpdate.as_view()), name='schoolyear_update'),
    path('schoolyears/<int:pk>/delete', login_required(views.SchoolYearDelete.as_view()), name='schoolyear_delete'),

    path('students', login_required(views.StudentList.as_view()), name='student_list'),
    path('students/create', login_required(views.StudentCreate.as_view()), name='student_create'),
    path('students/<int:pk>/update', login_required(views.StudentUpdate.as_view()), name='student_update'),
    path('students/<int:pk>/delete', login_required(views.StudentDelete.as_view()), name='student_delete'),

    path('teachers', login_required(views.TeacherList.as_view()), name='teacher_list'),
    path('teachers/create', login_required(views.TeacherCreate.as_view()), name='teacher_create'),
    path('teachers/<int:pk>/update', login_required(views.TeacherUpdate.as_view()), name='teacher_update'),
    path('teachers/<int:pk>/delete', login_required(views.TeacherDelete.as_view()), name='teacher_delete'),

    path('reports/study_results', login_required(views.StudyResultsReportView.as_view()), name='report_study_results'),
    path('reports/study_level', login_required(views.StudyLevelReportView.as_view()), name='report_study_level'),
    path('reports/klass_study_level', login_required(views.KlassStudyLevelReportView.as_view()), name='report_klass_study_level'),
    path('reports/klass_attendance', login_required(views.KlassAttendanceReportView.as_view()), name='report_klass_attendance'),
    path('reports/total_study_results', login_required(views.TotalStudyResultsReportView.as_view()), name='report_total_study_results'),
    path('reports/total_study_level', login_required(views.TotalStudyLevelReportView.as_view()), name='report_total_study_level'),
    path('reports/total_attendance', login_required(views.TotalAttendanceReportView.as_view()), name='report_total_attendance'),
]