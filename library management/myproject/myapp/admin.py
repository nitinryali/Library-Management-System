from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin


from .models import Attendance,vacancies1,Books,student,papers,papers1
@admin.register(Attendance)
@admin.register(student)

@admin.register(vacancies1)
@admin.register(Books)
@admin.register(papers)
@admin.register(papers1)
class PersonAdmin(ImportExportModelAdmin):
    pass
