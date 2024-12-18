from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Teacher, Subject, SubjectAssignment,SubjectRegistration
from students.models import AcademicYear, Student,Grade
from students.forms import StudentForm

from .forms import TeacherForm, SubjectForm, Assign_teacherForm, AcademicYearForm, SubjectRegistrationForm

# Create your views here.
def index_teacher(request):
    return render(request, 'teachers/index_teacher.html', {
        'teachers': Teacher.objects.all()
    })

def view_teacher(request, id):
    teacher = Teacher.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index_teacher'))


def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            new_firstname = form.cleaned_data['firstname']
            new_lastname = form.cleaned_data['lastname']
            new_title = form.cleaned_data['title']
            new_gender = form.cleaned_data['gender']
            new_email = form.cleaned_data['email']
            new_phone_number = form.cleaned_data['phone_number']
            new_marital_status = form.cleaned_data['marital_status']
            new_date_of_birth = form.cleaned_data['date_of_birth']

            new_student = Teacher(
                firstname = new_firstname,
                lastname = new_lastname,
                title = new_title,
                gender = new_gender,
                email = new_email,
                phone_number = new_phone_number,
                marital_status = new_marital_status,
                date_of_birth = new_date_of_birth,

            )

            new_student.save()
            return render(request, 'teachers/add_teacher.html',{
                'form': TeacherForm(),
                'success': True

            })
    else:
        form = TeacherForm()
    return render(request, 'teachers/add_teacher.html', {
        'form': TeacherForm()
    })


def edit_teacher(request, id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return render(request, 'teachers/edit_teacher.html', {
                'form': form,
                'success': True
            })
    else:
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(instance=teacher)
    return  render(request, 'teachers/edit_teacher.html', {
            'form': form

    })

def delete_teacher(request, teacher_id):
    teacher= Teacher.objects.get(pk=teacher_id)
    if request.method == "POST":
        teacher.delete()
        messages.success(request, 'Teacher deleted successfully!')
        return redirect('index_teacher')

def subject(request):
    return render(request, 'teachers/subject.html', {
        'subjects': Subject.objects.all()
    })

def view_subject(request, id):
    subject = Subject.objects.get(pk=id)
    return HttpResponseRedirect(reverse('subject'))


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            new_subject_name = form.cleaned_data['subject_name']

            new_subject = Subject(
                subject_name = new_subject_name
            )

            new_subject.save()
            return render(request, 'teachers/add_subject.html',{
                'form': SubjectForm(),
                'success': True

            })
    else:
        form = SubjectForm()
    return render(request, 'teachers/add_subject.html', {
        'form': SubjectForm()
    })


def edit_subject(request, id):
    if request.method == 'POST':
        subject = Subject.objects.get(pk=id)
        form = SubjectForm(request.POST, instance=subject)

        if form.is_valid():
            form.save()
            return render(request, 'teachers/edit_subject.html', {
                'form': form,
                'success': True
            })

    else:
        subject = Subject.objects.get(pk=id)
        form = SubjectForm(instance=subject)

    return  render(request, 'teachers/edit_subject.html', {
            'form': form

    })

def subject_assignment(request, subject_name, academic_year_id):
    table_subject_object = Subject.objects.get(subject_name=subject_name)
    academic_year = AcademicYear.objects.get(id=academic_year_id)
    return render(request, 'teachers/subject_assignment.html/', {

        'subject_assign': SubjectAssignment.objects.filter(subject=table_subject_object, academic_year=academic_year_id),
        'subject_name': subject_name,
        'academic_year':academic_year

    })

def subject_assignment_academic(request, subject_name):
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            academic_year = form.cleaned_data['academic_year']
            academic_year_id=academic_year.id
            # Do something with the selected academic_year, like redirecting
            return redirect('subject_assignment', subject_name, academic_year_id)

    else:
        form = AcademicYearForm()
    return render(request, 'teachers/subject_assignment_academic.html', {
        'form': form,
        'subject_name': subject_name
    })

def assign_teacher(request):
    if request.method == 'POST':
        form = Assign_teacherForm(request.POST)
        if form.is_valid():
            new_teacher_name = form.cleaned_data['teacher_name']
            new_subject = form.cleaned_data['subject']
            new_grade_name = form.cleaned_data['grade_name']
            new_academic_year = form.cleaned_data['academic_year']

            new_assign = SubjectAssignment(
                teacher_name = new_teacher_name,
                subject=new_subject,
                grade_name = new_grade_name,
                academic_year = new_academic_year

            )

            new_assign.save()
            return render(request, 'teachers/assign_teacher.html', {
                'form': Assign_teacherForm(),
                'success': True

            })
    else:
        form = Assign_teacherForm()
    return render(request, 'teachers/assign_teacher.html', {
        'form': Assign_teacherForm()
    })

def edit_assign(request, id, academic_year_id):
    academic_year = AcademicYear.objects.get(id=academic_year_id)
    if request.method == 'POST':
        assign = SubjectAssignment.objects.get(pk=id)
        form = Assign_teacherForm(request.POST, instance=assign)

        if form.is_valid():
            form.save()
            return render(request, 'teachers/edit_assign.html', {
                'subject_one': SubjectAssignment.objects.get(pk=id),
                'form': form,
                'success': True,
                'academic_year': academic_year
            })

    else:
        assign = SubjectAssignment.objects.get(pk=id)
        form = Assign_teacherForm(instance=assign)

    return  render(request, 'teachers/edit_assign.html', {
        'subject_one': SubjectAssignment.objects.get(pk=id),
        'form': form,
        'academic_year': academic_year

    })

# Teacher dashboard Views
def teacher_dash(request):

    return render(request, 'teachers/teacher_dash.html', {

    })

def subject_academic_year(request):
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            academic_year = form.cleaned_data['academic_year']

            # Do something with the selected academic_year, like redirecting
            return redirect('teacher_subjects', academic_year_id=academic_year.id)

    else:
        form = AcademicYearForm()
    return render(request, 'teachers/subject_academic_year.html', {
        'form': form
    })

def form_class_academic_year(request):
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            academic_year = form.cleaned_data['academic_year']

            # Do something with the selected academic_year, like redirecting
            return redirect('form_class', academic_year_id=academic_year.id)

    else:
        form = AcademicYearForm()
    return render(request, 'teachers/form_class_academic_year.html', {
        'form': form
    })
def form_class(request, academic_year_id):
    teacher = Teacher.objects.get(email=request.session.get('email'))
    grades = Grade.objects.get(class_teacher=teacher.pk)
    academic_year = AcademicYear.objects.get(id=academic_year_id)

    return render(request, 'teachers/form_class.html',{
        'students': Student.objects.filter(academic_year=academic_year_id, grade=grades),
        'academic_year': academic_year,
    })

def view_form_student_grade(request, id, academic_year_id, class_name):
    academic_year = AcademicYear.objects.get(id=academic_year_id)
    table_grade_object = Grade.objects.get(class_name=class_name)
    student = Student.objects.get(pk=id)

    scores = SubjectRegistration.objects.filter(stud_name=student, grade_name=table_grade_object, academic_year=academic_year_id)
    return HttpResponseRedirect(reverse('form_class'))

def form_class_edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'teachers/form_class_edit.html', {
                'student_one': Student.objects.get(pk=id),
                'form': form,
                'success': True
            })
        return redirect('index')
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return  render(request, 'teachers/form_class_edit.html', {
            'student_one': Student.objects.get(pk=id),
            'form': form

    })

def teacher_subjects(request, academic_year_id):
    teacher = Teacher.objects.get(email=request.session.get('email'))
    academic_year = AcademicYear.objects.get(id=academic_year_id)
    return render(request, 'teachers/teacher_subjects.html', {
        'subjects': SubjectAssignment.objects.filter(academic_year=academic_year_id, teacher_name=teacher.pk),
        'academic_year': academic_year,
    })

def subject_students(request, academic_year_id, subject_name, class_name):
    table_grade_object = Grade.objects.get(class_name=class_name)
    academic_year = AcademicYear.objects.get(id=academic_year_id)
    subject_name_id = Subject.objects.get(subject_name=subject_name)
    return  render(request, 'teachers/subject_students.html',{
        'student_subject': SubjectRegistration.objects.filter(subject_name=subject_name_id, grade_name=table_grade_object, academic_year=academic_year_id),
        'academic_year': academic_year,
        'class_name': class_name,
        'subject_name': subject_name
    })

def subject_grades(request, academic_year_id, subject_name, class_name):
    table_grade_object = Grade.objects.get(class_name=class_name)
    academic_year = AcademicYear.objects.get(id=academic_year_id)
    subject_name_id = Subject.objects.get(subject_name=subject_name)
    return  render(request, 'teachers/subject_grades.html',{
        'student_subject': SubjectRegistration.objects.filter(subject_name=subject_name_id, grade_name=table_grade_object, academic_year=academic_year_id),
        'academic_year': academic_year,
        'class_name': class_name,
        'subject_name': subject_name
    })



def subject_register(request, academic_year_id, class_name, subject_name):
    # Example values

    academic_year = AcademicYear.objects.get(id=academic_year_id)
    s_name = Subject.objects.get(subject_name=subject_name)
    grade_name = Grade.objects.get(class_name=class_name)

    if request.method == "POST":
        form = SubjectRegistrationForm(request.POST, grade_name=grade_name, grade_name_value=grade_name, academic_year_value=academic_year,
                                       subject_name_value=s_name)
        if form.is_valid():
            form.save()
            return render(request, 'teachers/subject_register.html', {
                'form': form,
                'academic_year':academic_year,
                'subject': s_name,
                'class_name': grade_name,
                'success': True
            })
    else:
        form = SubjectRegistrationForm(grade_name=grade_name, grade_name_value=grade_name, academic_year_value=academic_year,
                                       subject_name_value=s_name)

    return render(request, 'teachers/subject_register.html', {
        'form': form,
        'academic_year': academic_year,
        'subject': s_name,
        'class_name': grade_name,

    })

def unregister(request, student_id):
    student = SubjectRegistration.objects.get(pk=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Student Unregistered to the Subject successfully!')
        return redirect('subject_students', academic_year_id=student.academic_year.id, subject_name=student.subject_name, class_name=student.grade_name)

def edit_grade(request, id):
    if request.method == 'POST':
        student_sub = SubjectRegistration.objects.get(pk=id)
        form = SubjectRegistrationForm(request.POST, instance=student_sub)
        if form.is_valid():
            form.save()
            return render(request, 'teachers/edit_grade.html', {
                'Student_Subject': student_sub,
                'form': form,
                'success': True
            })
    else:
        student_sub = SubjectRegistration.objects.get(pk=id)
        form = SubjectRegistrationForm(instance=student_sub)
    return  render(request, 'teachers/edit_grade.html', {
            'Student_Subject':student_sub,
            'form': form

    })

def edit_grade_2(request, id):
    if request.method == 'POST':
        student_sub = SubjectRegistration.objects.get(pk=id)
        form = SubjectRegistrationForm(request.POST, instance=student_sub)
        if form.is_valid():
            form.save()
            return render(request, 'teachers/edit_grade_2.html', {
                'Student_Subject': student_sub,
                'form': form,
                'success': True
            })
    else:
        student_sub = SubjectRegistration.objects.get(pk=id)
        form = SubjectRegistrationForm(instance=student_sub)
    return  render(request, 'teachers/edit_grade_2.html', {
            'Student_Subject':student_sub,
            'form': form

    })

def student_grades(request,class_name, academic_year_id):
    academic_year = AcademicYear.objects.get(id=academic_year_id)
    table_grade_object = Grade.objects.get(class_name=class_name)
    scores = SubjectRegistration.objects.filter(grade_name=table_grade_object, academic_year=academic_year_id)


    return render(request, 'teachers/student_grades.html', {
        'subjects': Subject.objects.all(),
        'students': scores,

    })
