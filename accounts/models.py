from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):

    course_name = models.CharField(max_length=200, null=True )
    course_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.course_name


class Professor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=11, null=True)
    name = models.CharField(max_length= 200, null=True)
    email = models.EmailField(max_length=250, null=True)
    courses = models.ForeignKey(Course , null= True , on_delete=models.SET_NULL)
    profile_pic = models.ImageField(null= True , blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User , null=True , on_delete=models.CASCADE)
    id_number = models.CharField(max_length=11 , null=True)
    name = models.CharField(max_length= 200, null=True)
    email = models.EmailField(max_length=250 , null=True)
    professors = models.ManyToManyField(Course)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name