from django.db import models
from  datetime import  datetime
class AcademicYear(models.Model):
    TERM_CHOICES = (
        ('Term 1', 'Term 1'),
        ('Term 2', 'Term 2'),
        ('Term 3', 'Term 3'),
    )
    year = models.CharField(max_length=200, null=True)
    term = models.CharField(max_length=50, choices=TERM_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together =('year', 'term')

    def __str__(self):
        return self.year+" "+self.term

class Grade(models.Model):
    class_name = models.CharField(max_length=100, null=True)
    class_teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.class_name



class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    STATUS_CHOICE = (
        ('Parents', 'Parents'),
        ('Guardians', 'Guardians'),
        ('Sibling', 'Sibling'),
    )
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='student_academic_year'
    )
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    live_with = models.CharField(max_length=100, choices=STATUS_CHOICE, default="Parents")
    date_of_birth = models.DateField()
    live_with_fullname = models.CharField(max_length=200, null=True)
    live_with_phone = models.CharField(max_length=200, null=True)
    live_with_address = models.TextField(max_length=400, null=True)
    sponsor_name =  models.TextField(max_length=400, null=True)
    sponsor_phone = models.TextField(max_length=400, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class StudentAttendance(models.Model):
    DAYS_CHOICE = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    )
    STATUS_CHOICE = (
        ('P', 'P'),
        ('A', 'A'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    class_attended = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
    week = models.IntegerField(null=True)
    day = models.CharField(max_length=200, choices=DAYS_CHOICE)
    status = models.CharField(max_length=200, choices=STATUS_CHOICE)
    date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student}  on {self.day}"



