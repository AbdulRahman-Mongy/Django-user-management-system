from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['profile_pic']


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['profile_pic']