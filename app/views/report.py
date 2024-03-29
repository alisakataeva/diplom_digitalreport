from datetime import datetime

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from app.models import Plan, ClassbookNote, Student, Klass, Subject
from app.mixins import ContextMixin

# Create your views here.


# Прохождение учебного материала
class StudyResultsReportView(ContextMixin, TemplateView):
    template_name = "reports/study_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        plans = Plan.objects.all()

        if context.get('current_teacher') and context.get('system_role') != 'vice_principal':
            try:
                subjects = Subject.objects.filter(teacher=context.get('current_teacher'))
                plans = plans.filter(subject__in=subjects)
            except Subject.DoesNotExist:
                plans = []

        # START Filtering

        if plans:

            all_years = []
            all_periods = []
            all_klasses = []

            for plan in plans:
                if (str(plan.schoolyear.nach_g.year), str(plan.schoolyear.kon_g.year)) not in all_years:
                    all_years.append( (str(plan.schoolyear.nach_g.year), str(plan.schoolyear.kon_g.year)) )
                if (plan.n_ob, plan.k_ob) not in all_periods:
                    all_periods.append( (plan.n_ob, plan.k_ob) )
                if plan.schoolyear.klass not in all_klasses:
                    all_klasses.append( plan.schoolyear.klass )

            selected_period = self.request.GET.get('period')
            selected_klass = self.request.GET.get('klass')

            if selected_period:
                if '-' in selected_period:
                    try:
                        start, end = selected_period.split("_")[0], selected_period.split("_")[1]

                        start = datetime.strptime(start, '%Y-%m-%d')
                        end = datetime.strptime(end, '%Y-%m-%d')

                        plans = plans.filter(n_ob=start, k_ob=end)
                    except Exception as e:
                        pass
                else:
                    try:
                        start, end = selected_period.split("_")[0], selected_period.split("_")[1]

                        start = datetime.strptime(start, '%Y').year
                        end = datetime.strptime(end, '%Y').year

                        plans = plans.filter(schoolyear__nach_g__year=start, schoolyear__kon_g__year=end)
                    except Exception as e:
                        pass


            if selected_klass: 
                try:
                    klass = Klass.objects.get(pk=int( selected_klass ))
                    plans = plans.filter(schoolyear__klass=klass)
                except Exception as e:
                    pass

            context['years'] = all_years
            context['periods'] = all_periods
            context['klasses'] = all_klasses

        # END Filtering

        total_hours = 0
        total_used = 0
        total_diff = 0

        for plan in plans:

            hours = plan.kol_ch
            used = []
            for lsn in ClassbookNote.objects.filter(program__plan=plan):
                if (lsn.data_z, lsn.time_z) not in used:
                    used.append((lsn.data_z, lsn.time_z))
            diff = len(used) - hours

            total_hours += hours
            total_used += len(used)
            total_diff += diff

            plan.used_hours = len(used)
            plan.hours_diff = diff

        context['rows'] = plans
        context['total_hours'] = total_hours
        context['total_used'] = total_used
        context['total_diff'] = total_diff

        return context


# Успеваемость по предметам
class StudyLevelReportView(ContextMixin, TemplateView):
    template_name = "reports/study_level.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        plans = Plan.objects.all().order_by("n_ob")

        if context.get('current_teacher') and context.get('system_role') != 'vice_principal':
            try:
                subjects = Subject.objects.filter(teacher=context.get('current_teacher'))
                plans = plans.filter(subject__in=subjects)
            except Subject.DoesNotExist:
                plans = []

        # START Filtering

        if plans:

            all_years = []
            all_periods = []
            all_klasses = []


            for plan in plans:
                if (str(plan.schoolyear.nach_g.year), str(plan.schoolyear.kon_g.year)) not in all_years:
                    all_years.append( (str(plan.schoolyear.nach_g.year), str(plan.schoolyear.kon_g.year)) )
                if (plan.n_ob, plan.k_ob) not in all_periods:
                    all_periods.append((plan.n_ob, plan.k_ob))
                if plan.schoolyear.klass not in all_klasses:
                    all_klasses.append( plan.schoolyear.klass )

            selected_period = self.request.GET.get('period')
            selected_klass = self.request.GET.get('klass')

            if selected_period:
                if '-' in selected_period:
                    try:
                        start, end = selected_period.split("_")[0], selected_period.split("_")[1]

                        start = datetime.strptime(start, '%Y-%m-%d')
                        end = datetime.strptime(end, '%Y-%m-%d')

                        plans = plans.filter(n_ob=start, k_ob=end)
                    except Exception as e:
                        pass
                else:
                    try:
                        start, end = selected_period.split("_")[0], selected_period.split("_")[1]

                        start = datetime.strptime(start, '%Y').year
                        end = datetime.strptime(end, '%Y').year

                        plans = plans.filter(schoolyear__nach_g__year=start, schoolyear__kon_g__year=end)
                    except Exception as e:
                        pass

            if selected_klass: 
                try:
                    klass = Klass.objects.get(pk=int( selected_klass ))
                    plans = plans.filter(schoolyear__klass=klass)
                except Exception as e:
                    pass

            context['years'] = all_years
            context['periods'] = all_periods
            context['klasses'] = all_klasses

        # END Filtering

        total = {
            5: 0,
            4: 0,
            3: 0,
            2: 0,
            'students': 0
        }
        
        for plan in plans:

            lessons = ClassbookNote.objects.filter(program__plan=plan)
            klass = plan.schoolyear.klass
            students_count = klass.student_set.all().count()

            total['students'] += students_count

            marks = {
                5: 0,
                4: 0,
                3: 0,
                2: 0,
            }

            for lsn in lessons:
                try:
                    period = int( lsn.prim )
                    mark = int( lsn.oc )
                    marks[mark] += 1
                    total[mark] += 1
                except:
                    pass

            plan.marks = marks

            if students_count > 0:
                plan.grades_quality = (marks[5] + marks[4]) / students_count * 100
                plan.grades_progress = (students_count - marks[2]) / students_count * 100
            else:
                plan.grades_quality = 0
                plan.grades_progress = 0

        context['rows'] = plans
        context['total_5'] = total[5]
        context['total_4'] = total[4]
        context['total_3'] = total[3]
        context['total_2'] = total[2]

        if total['students'] > 0:
            context['total_quality'] = (total[5] + total[4]) / total['students'] * 100
            context['total_progress'] = (total['students'] - total[2]) / total['students'] * 100
        else:
            context['total_quality'] = 0
            context['total_progress'] = 0

        return context


# Отчет кл.рук. об успеваемости
class KlassStudyLevelReportView(ContextMixin, TemplateView):
    template_name = "reports/klass_study_level.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        plans = Plan.objects.all().order_by("n_ob")

        if context['current_klass']:
            plans = plans.filter(schoolyear__klass=context['current_klass'])

        # START Filtering

        all_years = []
        all_periods = []
        all_klasses = []

        for plan in plans:
            if (str(plan.schoolyear.nach_g.year), str(plan.schoolyear.kon_g.year)) not in all_years:
                all_years.append( (str(plan.schoolyear.nach_g.year), str(plan.schoolyear.kon_g.year)) )
            if (plan.n_ob, plan.k_ob) not in all_periods:
                all_periods.append((plan.n_ob, plan.k_ob))
            if plan.schoolyear.klass not in all_klasses:
                all_klasses.append( plan.schoolyear.klass )

        selected_period = self.request.GET.get('period')
        selected_klass = self.request.GET.get('klass')

        if selected_period:
            if '-' in selected_period:
                try:
                    start, end = selected_period.split("_")[0], selected_period.split("_")[1]

                    start = datetime.strptime(start, '%Y-%m-%d')
                    end = datetime.strptime(end, '%Y-%m-%d')

                    plans = plans.filter(n_ob=start, k_ob=end)
                except Exception as e:
                    pass
            else:
                try:
                    start, end = selected_period.split("_")[0], selected_period.split("_")[1]

                    start = datetime.strptime(start, '%Y').year
                    end = datetime.strptime(end, '%Y').year

                    plans = plans.filter(schoolyear__nach_g__year=start, schoolyear__kon_g__year=end)
                except Exception as e:
                    pass

        if selected_klass: 
            try:
                klass = Klass.objects.get(pk=int( selected_klass ))
                plans = plans.filter(schoolyear__klass=klass)
            except Exception as e:
                pass

        context['years'] = all_years
        context['periods'] = all_periods
        context['klasses'] = all_klasses

        # END Filtering

        result_plans = {}

        for plan in plans:

            period = plan.display()
            klass = plan.schoolyear.klass

            if not result_plans.get(period + "_" + klass.get_number()):
                result_plans[period + "_" + klass.get_number()] = {
                    'objects': [],
                    'klass': klass,
                    'period': period
                }
            result_plans[period + "_" + klass.get_number()]['objects'].append( plan )

        total_grades = {
            5: 0,
            4: 0,
            3: 0,
            2: 0,
        }

        total_data = {
            'students_count': 0,

            'agrade_students': 0,
            'bgrade_students': 0,
            'one_cgrade_students': 0,
            'cgrade_students': 0,
            'dgrade_students': 0,

            'grades_quality': 0,
            'grades_progress': 0
        }

        for key, chunk in result_plans.items():

            teacher = "(кл.руководителя нет)"
            if chunk['klass'].teacher:
                teacher = chunk['klass'].teacher.display()

            all_marks = {
                5: 0,
                4: 0,
                3: 0,
                2: 0,
            }

            chunk_data = {

                'teacher': teacher,
                'klass': chunk['klass'].get_number(),
                'students_count': chunk['klass'].get_students_count(),

                'agrade_students': 0,
                'bgrade_students': 0,
                'one_cgrade_students': 0,
                'cgrade_students': 0,
                'dgrade_students': 0,

                'grades_quality': 0,
                'grades_progress': 0

            }

            total_data['students_count'] += chunk_data['students_count']

            students_marks = {}

            for student in Student.objects.filter(klass=chunk['klass']):
                students_marks[student.pk] = {
                    5: 0,
                    4: 0,
                    3: 0,
                    2: 0,
                }

            for plan in chunk['objects']:
                lessons = ClassbookNote.objects.filter(program__plan=plan)

                for lsn in lessons:
                    try:
                        period = int( lsn.prim )
                        students_marks[lsn.student.pk][int( lsn.oc )] += 1
                        all_marks[int( lsn.oc )] += 1
                        total_grades[int( lsn.oc )] += 1
                    except Exception as e:
                        pass

            for student_id, marks in students_marks.items():
                if marks[2] > 0:
                    chunk_data['dgrade_students'] += 1
                    total_data['dgrade_students'] += 1
                elif marks[3] > 1:
                    chunk_data['cgrade_students'] += 1
                    total_data['cgrade_students'] += 1
                elif marks[3] == 1:
                    chunk_data['one_cgrade_students'] += 1
                    total_data['one_cgrade_students'] += 1
                elif marks[4] > 0:
                    chunk_data['bgrade_students'] += 1
                    total_data['bgrade_students'] += 1
                elif marks[5] > 0:
                    chunk_data['agrade_students'] += 1
                    total_data['agrade_students'] += 1

            if chunk_data['students_count'] > 0:
                chunk_data['grades_quality'] = (all_marks[5] + all_marks[4]) / chunk_data['students_count'] * 100
                chunk_data['grades_progress'] = (chunk_data['students_count'] - all_marks[2]) / chunk_data['students_count'] * 100
            else:
                chunk_data['grades_quality'] = 0
                chunk_data['grades_progress'] = 0

            chunk['data'] = chunk_data

        context['rows'] = result_plans
        context['total_agrade_students'] = total_data['agrade_students']
        context['total_bgrade_students'] = total_data['bgrade_students']
        context['total_one_cgrade_students'] = total_data['one_cgrade_students']
        context['total_cgrade_students'] = total_data['cgrade_students']
        context['total_dgrade_students'] = total_data['dgrade_students']

        if total_data['students_count'] > 0:
            context['total_grades_quality'] = (total_grades[5] + total_grades[4]) / total_data['students_count'] * 100
            context['total_grades_progress'] = (total_data['students_count'] - total_grades[2]) / total_data['students_count'] * 100
        else:
            context['total_grades_quality'] = 0
            context['total_grades_progress'] = 0

        return context


class KlassAttendanceReportView(ContextMixin, TemplateView):
    template_name = "reports/klass_attendance.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        plans = Plan.objects.all().order_by("n_ob")
        if context['current_klass']:
            plans = plans.filter(schoolyear__klass=context['current_klass'])

        # START Filtering

        all_years = []
        all_periods = []
        all_klasses = []

        for plan in plans:
            if (str(plan.schoolyear.nach_g.year), str(plan.schoolyear.kon_g.year)) not in all_years:
                all_years.append( (str(plan.schoolyear.nach_g.year), str(plan.schoolyear.kon_g.year)) )
            if (plan.n_ob, plan.k_ob) not in all_periods:
                all_periods.append((plan.n_ob, plan.k_ob))
            if plan.schoolyear.klass not in all_klasses:
                all_klasses.append( plan.schoolyear.klass )

        selected_period = self.request.GET.get('period')
        selected_klass = self.request.GET.get('klass')

        if selected_period:
            if '-' in selected_period:
                try:
                    start, end = selected_period.split("_")[0], selected_period.split("_")[1]

                    start = datetime.strptime(start, '%Y-%m-%d')
                    end = datetime.strptime(end, '%Y-%m-%d')

                    plans = plans.filter(n_ob=start, k_ob=end)
                except Exception as e:
                    pass
            else:
                try:
                    start, end = selected_period.split("_")[0], selected_period.split("_")[1]

                    start = datetime.strptime(start, '%Y').year
                    end = datetime.strptime(end, '%Y').year

                    plans = plans.filter(schoolyear__nach_g__year=start, schoolyear__kon_g__year=end)
                except Exception as e:
                    pass

        if selected_klass: 
            try:
                klass = Klass.objects.get(pk=int( selected_klass ))
                plans = plans.filter(schoolyear__klass=klass)
            except Exception as e:
                pass

        context['years'] = all_years
        context['periods'] = all_periods
        context['klasses'] = all_klasses

        # END Filtering
        
        result_plans = {}

        for plan in plans:

            period = plan.display()
            klass = plan.schoolyear.klass

            if not result_plans.get(period + "_" + klass.get_number()):
                result_plans[period + "_" + klass.get_number()] = {
                    'objects': [],
                    'klass': klass,
                    'period': period
                }
            result_plans[period + "_" + klass.get_number()]['objects'].append( plan )

        total_data = {
            'skips_desease': 0,
            'skips_reasonable': 0,
            'skips': 0,
            'all_skips': 0,
        }

        for key, chunk in result_plans.items():

            teacher = "(кл.руководителя нет)"
            if chunk['klass'].teacher:
                teacher = chunk['klass'].teacher.display()

            chunk_data = {

                'teacher': teacher,
                'klass': chunk['klass'].get_number(),
                'students_count': chunk['klass'].get_students_count(),
                'students': {},

                'total_skips_desease': 0,
                'total_skips_reasonable': 0,
                'total_skips': 0,
                'total_all_skips': 0,

            }

            for student in Student.objects.filter(klass=chunk['klass']):
                chunk_data['students'][student.pk] = {
                    'name': student.display(),

                    'skips_desease': 0,
                    'skips_reasonable': 0,
                    'skips': 0,
                    'all_skips': 0,
                }

            for plan in chunk['objects']:
                lessons = ClassbookNote.objects.filter(program__plan=plan, student__klass=chunk['klass'])

                for lsn in lessons:
                    attendance = lsn.pris
                    if attendance != 'ATTEND':
                        if attendance == 'ABSENT':
                            chunk_data['students'][lsn.student.pk]['skips'] += 1
                        elif attendance == 'REASONABLE_ABSENT':
                            chunk_data['students'][lsn.student.pk]['skips_reasonable'] += 1
                        elif attendance == 'WAS_ILL':
                            chunk_data['students'][lsn.student.pk]['skips_desease'] += 1

                        chunk_data['students'][lsn.student.pk]['all_skips'] += 1

            for student in chunk_data['students'].values():
                chunk_data['total_skips_desease'] += student['skips_desease']
                total_data['skips_desease'] += student['skips_desease']

                chunk_data['total_skips_reasonable'] += student['skips_reasonable']
                total_data['skips_reasonable'] += student['skips_reasonable']

                chunk_data['total_skips'] += student['skips']
                total_data['skips'] += student['skips']

                chunk_data['total_all_skips'] += student['all_skips']
                total_data['all_skips'] += student['all_skips']

            chunk['data'] = chunk_data

        context['rows'] = result_plans
        context['total_skips_desease'] = total_data['skips_desease']
        context['total_skips_reasonable'] = total_data['skips_reasonable']
        context['total_skips'] = total_data['skips']
        context['total_all_skips'] = total_data['all_skips']

        return context


class TotalStudyResultsReportView(ContextMixin, TemplateView):
    template_name = "reports/total_study_results.html"


class TotalStudyLevelReportView(ContextMixin, TemplateView):
    template_name = "reports/total_study_level.html"


class TotalAttendanceReportView(ContextMixin, TemplateView):
    template_name = "reports/total_attendance.html"
