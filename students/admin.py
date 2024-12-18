from django.contrib import admin
from .models import Student, Grade, StudentAttendance,AcademicYear

# Register your models here.
admin.site.register(AcademicYear)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(StudentAttendance)
