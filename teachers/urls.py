from django.urls import path
from . import views

urlpatterns = [
    path('index_teacher/', views.index_teacher, name='index_teacher'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('edit_teacher/<int:id>/', views.edit_teacher, name='edit_teacher'),
    path('delete_teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('unregister/<int:student_id>/', views.unregister, name='unregister'),
    path('<int:id>', views.view_teacher, name='view_teacher'),
    path('subject/', views.subject, name='subject'),
    path('assign_teacher/', views.assign_teacher, name='assign_teacher'),
    path('subject_assignment/<str:subject_name>/<int:academic_year_id>', views.subject_assignment, name='subject_assignment'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('edit_subject/<int:id>/', views.edit_subject, name='edit_subject'),
    path('subject_grades/<int:academic_year_id>/<str:subject_name>/<str:class_name>', views.subject_grades, name='subject_grades'),
    path('edit_assign/<int:id>/<int:academic_year_id>', views.edit_assign, name='edit_assign'),
   path('<int:id>', views.view_subject, name='view_subject'),

    # paths for teacher dash

    path('teacher_dash/', views.teacher_dash, name='teacher_dash'),
    path('subject_academic_year', views.subject_academic_year, name='subject_academic_year'),
    path('form_class/<int:academic_year_id>', views.form_class, name='form_class'),
    path('form_class_edit/<int:id>', views.form_class_edit, name='form_class_edit'),
    path('student_grades/<str:class_name>/<int:academic_year_id>', views.student_grades, name='student_grades'),
    path('form_class_academic_year', views.form_class_academic_year, name='form_class_academic_year'),
    path('teacher_subjects/<int:academic_year_id>', views.teacher_subjects, name='teacher_subjects'),
    path('subject_students/<int:academic_year_id>/<str:subject_name>/<str:class_name>', views.subject_students, name='subject_students'),
    path('subject_register/<int:academic_year_id>/<str:class_name>/<str:subject_name>', views.subject_register, name='subject_register'),
    path('edit_grade/<int:id>/', views.edit_grade, name='edit_grade'),
    path('edit_grade_2/<int:id>/', views.edit_grade_2, name='edit_grade_2'),
    path('<int:id>/<int:academic_year_id>/<str:class_name>', views.view_form_student_grade, name='view_form_student_grade')
]