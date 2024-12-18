from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student, Grade, AcademicYear
from .forms import StudentForm,AcademicYearForm
from django.contrib import messages
from django.http import JsonResponse

shared_x = None

def dashboard(request):
    return render(request, 'students/dashboard.html', {

    })

# Create your views here.
def chart_data_api(request):
    # Query data from your model (for example, return field1 and field2)
    data = ""

    # Convert the QuerySet to a list (or other JSON-serializable format)
    data_list = list(data)

    # Return the data as JSON response
    return JsonResponse({'data': data_list})

def home(request):
    return render(request, 'students/home.html', {})

def registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_firstname = form.cleaned_data['firstname']
            new_lastname = form.cleaned_data['lastname']
            new_grade = form.cleaned_data['grade']
            new_academic_year = form.cleaned_data['academic_year']
            new_gender = form.cleaned_data['gender']
            new_live_with = form.cleaned_data['live_with']
            new_date_of_birth = form.cleaned_data['date_of_birth']
            new_live_with_fullname = form.cleaned_data['live_with_fullname']
            new_live_with_phone = form.cleaned_data['live_with_phone']
            new_live_with_address = form.cleaned_data['live_with_address']
            new_sponsor_name = form.cleaned_data['sponsor_name']
            new_sponsor_phone = form.cleaned_data['sponsor_phone']

            new_student = Student(
                firstname = new_firstname,
                lastname = new_lastname,
                grade = new_grade,
                academic_year=new_academic_year,
                gender = new_gender,
                live_with = new_live_with,
                date_of_birth = new_date_of_birth,
                live_with_fullname = new_live_with_fullname,
                live_with_phone = new_live_with_phone,
                live_with_address = new_live_with_address,
                sponsor_name = new_sponsor_name,
                sponsor_phone = new_sponsor_phone

            )

            new_student.save()
            return render(request,'students/registration.html',{
                'form': StudentForm(),
                'success': True

            })

    else:
        form = StudentForm()
    return render(request, 'students/registration.html', {
        'form': StudentForm()
    })


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_firstname = form.cleaned_data['firstname']
            new_lastname = form.cleaned_data['lastname']
            new_grade = form.cleaned_data['grade']
            new_gender = form.cleaned_data['gender']
            new_live_with = form.cleaned_data['live_with']
            new_date_of_birth = form.cleaned_data['date_of_birth']

            new_student = Student(
                firstname = new_firstname,
                lastname = new_lastname,
                grade = new_grade,
                gender = new_gender,
                live_with = new_live_with,
                date_of_birth = new_date_of_birth,

            )

            new_student.save()
            return render(request,'students/add.html',{
                'form': StudentForm(),
                'success': True

            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {
        'form': StudentForm()
    })


def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'student_one': Student.objects.get(pk=id),
                'form': form,
                'success': True
            })
        return redirect('index')
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return  render(request, 'students/edit.html', {
            'student_one': Student.objects.get(pk=id),
            'form': form

    })

def delete_student(request, student_id):
    student= Student.objects.get(pk=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('index', class_name = student.grade, academic_year_id=student.academic_year.id)

def select_academic_year(request):
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            academic_year = form.cleaned_data['academic_year']

            # Do something with the selected academic_year, like redirecting
            return redirect('classes', academic_year_id=academic_year.id)

    else:
        form = AcademicYearForm()
    return render(request, 'students/select_academic_year.html', {
        'form': form
    })

def Academic_Year(request):
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            academic_year = form.cleaned_data['academic_year']
            request.session['academic_year_id'] = academic_year.id
            academic_year_name = AcademicYear.objects.get(id=academic_year.id)
            request.session['academic_year_name'] = academic_year.year
            request.session['academic_year_term'] = academic_year.term

            # Do something with the selected academic_year, like redirecting
            return redirect('dashboard')

    else:
        form = AcademicYearForm()
    return render(request, 'students/Academic_Year.html', {
        'form': form
    })

def classes(request,academic_year_id ):
    academic_year = AcademicYear.objects.get(id=academic_year_id)
    return render(request, 'students/classes.html', {
        'grades': Grade.objects.all(),
        'academic_year': academic_year,
        'academic_year_id': academic_year_id

    })

def index(request, class_name, academic_year_id):
    table_grade_object = Grade.objects.get(class_name=class_name)
    academic_year = AcademicYear.objects.get(id=academic_year_id)
    return render(request, 'students/index.html/', {

        'students': Student.objects.filter(grade=table_grade_object,academic_year=academic_year_id),
        'academic_year': academic_year,
        'class_name': class_name,


    })

