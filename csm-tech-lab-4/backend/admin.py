from django.contrib import admin

from .models import User, Student, Mentor, Section, Course, Attendance

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', "user","section", "course",'active', "banned"]

    actions = ['enroll']

    @admin.action(description='Enroll student into the section (Make is active)')
    def enroll(self, request, queryset):
        updated = queryset.update(active= True)
        # self.message_user(request, ngettext(
        #     '%d story was successfully marked as published.',
        #     '%d stories were successfully marked as published.',
        #     updated,
        # ) % updated, messages.SUCCESS)

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', "first_name","last_name", "username",'email']

class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', "user", "course"]

class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', "mentor", "capacity", "description"]

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', "name"]

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', "student", "date", "presence"]




admin.site.register(Student, StudentAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Attendance, AttendanceAdmin)