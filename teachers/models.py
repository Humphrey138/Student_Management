from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
# Create your models here.

class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    TITLE_CHOICES = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
    )
    STATUS_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widow', 'Widow'),
        ('Widower', 'Widower'),
    )

    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=10, null=True, choices=TITLE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.CharField(max_length=200, null=True, unique=True)
    phone_number = models.CharField(max_length=200, null=True)
    marital_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return str(self.lastname) if self.lastname else 'Just a Superuser'

class Department(models.Model):
    dept_name = models.CharField(max_length=200, null=True)
    dept_member = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dept_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_name

class GradeSubjects(models.Model):
    grade_name = models.ForeignKey('students.Grade', on_delete=models.CASCADE, null=True)
    grade_subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.grade_name) + " " + str(self.grade_subjects)


class SubjectRegistration(models.Model):
    stud_name = models.ForeignKey('students.Student', on_delete=models.CASCADE, null=True)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    grade_name = models.ForeignKey('students.Grade', on_delete=models.CASCADE, null=True)
    academic_year = models.ForeignKey('students.AcademicYear', on_delete=models.CASCADE, null=True)
    scores = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('stud_name', 'subject_name', 'academic_year')

    def __str__(self):
        return str(self.stud_name) + " " + str(self.subject_name)


class SchoolReport(models.Model):
    student_name = models.ForeignKey('students.Student', on_delete=models.CASCADE, null=True)
    grade_name = models.ForeignKey('students.Grade', on_delete=models.CASCADE, null=True)
    scores = models.IntegerField(null=True)
    signature = models.CharField(max_length=200, null=True)
    average_grade = models.IntegerField(null=True)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


class SubjectAssignment(models.Model):
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    grade_name = models.ForeignKey('students.Grade', on_delete=models.CASCADE, null=True)
    academic_year = models.ForeignKey('students.AcademicYear', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('teacher_name', 'subject', 'grade_name')

    def __str__(self):
        return f"{self.teacher_name} teaches {self.subject} in {self.grade_name}"
