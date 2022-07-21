#from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    username= models.CharField(max_length=200, unique=True)
    email= models.CharField(max_length=200)
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    section = models.ManyToManyField('Section')
    course = models.CharField(max_length=200, default="CS70")
    active = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Mentor(models.Model):
    user = models.ForeignKey(User, related_name='mentor', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='mentor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Section(models.Model):
    student_in_section = models.ManyToManyField(Student, related_name="sectionname")
    mentor = models.OneToOneField(Mentor, on_delete=models.CASCADE, primary_key=True)
    capacity = models.IntegerField()
    special = models.BooleanField(default=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Attendance(models.Model):
    student = models.ForeignKey(Student, related_name='attendance', on_delete=models.PROTECT)
    user_type = models.CharField(max_length=2, choices=[('P', 'Present'),('UA', 'Unexcused Absesnce'),('EA', "Excused Absence")])

    def __str__(self):
        return self.name
