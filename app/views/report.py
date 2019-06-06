from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from app.models import Plan, ClassbookNote
from app.mixins import ContextMixin

# Create your views here.


class StudyResultsReportView(ContextMixin, TemplateView):
    template_name = "reports/study_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        plans = Plan.objects.all()
        for plan in plans:
            hours = plan.kol_ch
            used = ClassbookNote.objects.filter(program__plan=plan).count()
            plan.used_hours = used
            plan.hours_diff = hours - used

        context['rows'] = plans

        return context


class StudyLevelReportView(ContextMixin, TemplateView):
    template_name = "reports/study_level.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        plans = Plan.objects.all()
        for plan in plans:

            lessons = ClassbookNote.objects.filter(program__plan=plan)
            klass = plan.schoolyear.klass
            students_count = klass.student_set.all().count()

            marks = {
                5: 0,
                4: 0,
                3: 0,
                2: 0,
            }

            for lsn in lessons:
                try:
                    mark = int( lsn.oc )
                    marks[mark] += 1
                except:
                    pass

            plan.marks = marks
            plan.grades_quality = (marks[5] + marks[4]) / students_count * 100
            plan.grades_progress = (students_count - marks[2]) / students_count * 100

        context['rows'] = plans

        return context


class StudyResultsReportView(ContextMixin, TemplateView):
    template_name = "reports/study_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        plans = Plan.objects.all()
        for plan in plans:
            hours = plan.kol_ch
            used = ClassbookNote.objects.filter(program__plan=plan).count()
            plan.used_hours = used
            plan.hours_diff = hours - used

        context['rows'] = plans

        return context


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