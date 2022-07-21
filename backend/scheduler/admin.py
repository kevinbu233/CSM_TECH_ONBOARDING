from django.contrib import admin

from .models import User, Student, Section, Mentor, Attendance

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Section)
admin.site.register(Mentor)
admin.site.register(Attendance)
