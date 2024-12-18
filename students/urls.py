from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/chart-data/', views.chart_data_api, name='chart_data_api'),
    path('index/<str:class_name>/<int:academic_year_id>/', views.index, name='index'),
    path('classes/<int:academic_year_id>', views.classes, name='classes'),
    path('Academic_year/', views.Academic_Year, name='Academic_Year'),
    path('<int:id>', views.view_student, name='view_student'),
    path('registration/', views.registration, name='registration'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),

]