from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from teachers.models import Teacher

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            request.session['is_teacher'] = hasattr(user, 'teacher')

            if request.session['is_teacher']:
                return redirect('teacher_dash')
            else:
                return redirect('Academic_Year')
        else:
            messages.success(request, ("There was an error Logging in, Try Again..."))
            return redirect('login_user')
    return render(request, 'authentication/login_user.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')