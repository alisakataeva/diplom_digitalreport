from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from app.models import SchoolYear
from app.mixins import ContextMixin

# Create your views here.


class StudyResultsReportView(ContextMixin, TemplateView):
    template_name = "reports/study_results.html"


class StudyLevelReportView(ContextMixin, TemplateView):
    template_name = "reports/study_level.html"


class KlassStudyLevelReportView(ContextMixin, TemplateView):
    template_name = "reports/klass_study_level.html"


class KlassAttendanceReportView(ContextMixin, TemplateView):
    template_name = "reports/klass_attendance.html"


class TotalStudyResultsReportView(ContextMixin, TemplateView):
    template_name = "reports/total_study_results.html"


class TotalStudyLevelReportView(ContextMixin, TemplateView):
    template_name = "reports/total_study_level.html"


class TotalAttendanceReportView(ContextMixin, TemplateView):
    template_name = "reports/total_attendance.html"