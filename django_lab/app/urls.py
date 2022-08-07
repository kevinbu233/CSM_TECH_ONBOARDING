from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.getAllUsers, name='users'),
    path('students/', views.getAllStudents, name='students'),
    path('mentors/', views.getAllMentors, name='mentors'),
    path('sections/', views.getAllSections, name='sections'),
    path('sections/<section_id>/students', views.getStudents, name='students'),
    path('sections/<section_id>/details', views.sectionDetail, name='sectionDetail'),
]