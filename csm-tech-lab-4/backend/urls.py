from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users),
    path('sections/', views.sections),
    path('sections/<int:section_id>/students/', views.section_students),
    path('sections/<int:section_id>/details/', views.section_details),
    path('students/<int:student_id>/details/', views.student_details),
    path('attendances/<int:attendance_id>/details/', views.attendance_details),
    path('attendances/<int:student_id>/', views.attendance_student),
]