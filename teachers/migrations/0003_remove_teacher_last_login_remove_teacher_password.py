# Generated by Django 5.0.7 on 2024-07-29 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teacher_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='password',
        ),
    ]