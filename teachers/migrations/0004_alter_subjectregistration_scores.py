# Generated by Django 5.0.7 on 2024-08-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_remove_teacher_last_login_remove_teacher_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectregistration',
            name='scores',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
