from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey("Section", on_delete=models.CASCADE)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    active = models.BooleanField()
    banned = models.BooleanField()

    def __str__(self):
        firstName = self.user.first_name
        lastName = self.user.last_name
        return f"{firstName} {lastName} ({self.id})"


class Mentor(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    def __str__(self):
        firstName = self.user.first_name
        lastName = self.user.last_name
        return f"{firstName} {lastName} ({self.id})"

class Section(models.Model):
    mentor = models.OneToOneField("Mentor", on_delete=models.CASCADE)

    capacity = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        firstName = self.mentor.user.first_name
        lastName = self.mentor.user.last_name
        return f"Section By {firstName} {lastName} (id: {self.id})"


class Course(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Attendance(models.Model):
    student = models.ForeignKey("Student", on_delete=models.PROTECT)
    date = models.DateField()
    presence= models.CharField(max_length=2, choices=[('PR', 'Present'),('UN', 'Unexcused Absesnce'),('EX', "Excused Absence")])

    def __str__(self):
        firstName = self.student.user.first_name
        lastName = self.student.user.last_name
        return f"{firstName} {lastName} {self.date}"
