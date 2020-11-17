from django.shortcuts import render , redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.restriction_decorators import *
from accounts.models import *
from django.contrib.auth.models import User


@login_required(login_url='login')
@is_restricted(allowed_roles=['admin'])
def home_page(request):
    students = Student.objects.all()
    professors = Professor.objects.all()
    context = {'students' : students ,
               'professors' : professors,
                }

    return render(request ,'accounts/Home_page.html' , context)


@is_logedin
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username , password= password)
        if user is not None:
            login(request , user)
            return redirect('home')

    return render(request ,'accounts/login.html' )


def logout_page(request):
    logout(request)
    return redirect('login')


@is_restricted(allowed_roles=['admin'])
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # create a student as this user
            if  request.POST.get('status') == 'student':
                student = Student()
                student.name = request.POST.get('username')
                student.user = User.objects.get(username=student.name)
                student.id_number = request.POST.get('id_number')
                student.save()
            # create a professor as this user
            if  request.POST.get('status') == 'professor':
                professor = Professor()
                professor.name = request.POST.get('username')
                professor.user = User.objects.get(username=professor.name)
                professor.id_number = request.POST.get('id_number')
                professor.save()

            messages.success(request , 'Your Account Was Created Successfully')
            return redirect('login')

    context = {'form': form}
    return render(request ,'accounts/register.html' , context)


def profile_page(request):
    try:
        student = request.user.student
        form = StudentForm(instance=student)
        if request.method == 'POST':
            form = StudentForm(request.POST , request.FILES, instance=student)
            if form.is_valid():
                form.save()

        context = {'user' : student ,
                   'form' : form,
                   }
    except:
        professor = request.user.professor
        form = ProfessorForm(instance=professor)
        if request.method == 'POST':
            form = ProfessorForm(request.POST, request.FILES, instance=professor)
            if form.is_valid():
                form.save()
        context = {'user': professor ,
                       'form' : form,
                       }

    return render(request ,'accounts/profile.html' , context)

