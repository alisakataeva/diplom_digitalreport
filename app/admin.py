from django.contrib import admin

from app import models

# Register your models here.


admin.site.register(models.Klass)
admin.site.register(models.Teacher)
admin.site.register(models.SchoolYear)
admin.site.register(models.Plan)
admin.site.register(models.Program)
admin.site.register(models.Subject)
admin.site.register(models.Student)
admin.site.register(models.ClassbookNote)