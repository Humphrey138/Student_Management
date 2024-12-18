# Generated by Django 5.0.7 on 2024-07-29 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='class_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='academic_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_academic_year', to='students.academicyear'),
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.grade'),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='class_attended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.grade'),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
    ]