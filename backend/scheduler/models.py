from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    section_name = models.ManyToManyField('Section')

    banned = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Mentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Section(models.Model):
    student_in_section = models.ManyToManyField(Student)
    mentor = models.OneToOneField(Mentor, on_delete=models.CASCADE, primary_key=True)
    capacity = models.IntegerField()
    special = models.BooleanField(default=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    user_type = models.CharField(max_length=2, choices=[('P', 'Present'),('UA', 'Unexcused Absesnce'),('EA', "Excused Absence")])

    def __str__(self):
        return self.name