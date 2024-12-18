from django.contrib import admin
from .models import Teacher, Department, Subject, SubjectRegistration, SubjectAssignment, GradeSubjects, SchoolReport

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(SubjectAssignment)
admin.site.register(SubjectRegistration)
admin.site.register(GradeSubjects)
admin.site.register(SchoolReport)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'is_staff', 'is_superuser')