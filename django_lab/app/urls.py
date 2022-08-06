from django.urls import path

from . import views

urlpatterns = [
    path('api/users/', views.getAllUsers, name='users'),
    path('api/students/', views.getAllStudents, name='students'),
    path('api/mentors/', views.getAllMentors, name='mentors'),
    path('api/sections/', views.getAllSections, name='sections'),
    path('api/sections/<section_id>/students', views.getStudents, name='students'),
    path('api/sections/<section_id>/details', views.sectionDetail, name='sectionDetail'),
]