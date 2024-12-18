# Generated by Django 5.0.7 on 2024-07-29 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], max_length=10, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('email', models.CharField(max_length=200, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=200, null=True)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widow', 'Widow'), ('Widower', 'Widower')], max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GradeSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('grade_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.grade')),
                ('grade_subjects', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('academic_year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.academicyear')),
                ('stud_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student')),
                ('subject_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.subject')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', models.IntegerField(null=True)),
                ('signature', models.CharField(max_length=200, null=True)),
                ('average_grade', models.IntegerField(null=True)),
                ('comment', models.TextField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('grade_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.grade')),
                ('student_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student')),
                ('subject_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.subject')),
                ('class_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('dept_member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('academic_year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.academicyear')),
                ('grade_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.grade')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.subject')),
                ('teacher_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
            options={
                'unique_together': {('teacher_name', 'subject', 'grade_name')},
            },
        ),
    ]