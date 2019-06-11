from .base import IndexView, LoginView, logout

from .classbooknote import ClassbookNoteList, ClassbookNoteCreate, ClassbookNoteUpdate, ClassbookNoteDelete
from .klass import KlassList, KlassCreate, KlassUpdate, KlassDelete
from .plan import PlanList, PlanCreate, PlanUpdate, PlanDelete
from .subject import SubjectList, SubjectCreate, SubjectUpdate, SubjectDelete
from .program import ProgramList, ProgramCreate, ProgramUpdate, ProgramDelete
from .schoolyear import SchoolYearList, SchoolYearCreate, SchoolYearUpdate, SchoolYearDelete
from .student import StudentList, StudentCreate, StudentUpdate, StudentDelete
from .teacher import TeacherList, TeacherCreate, TeacherUpdate, TeacherDelete

from .report import StudyLevelReportView, StudyResultsReportView, KlassAttendanceReportView, KlassStudyLevelReportView, \
    TotalStudyLevelReportView, TotalAttendanceReportView, TotalStudyResultsReportView