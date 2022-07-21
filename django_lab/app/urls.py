from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # ex: /polls/5/
    path('api/users/', views.getAllUsers, name='users'),
    path('api/students/', views.getAllStudents, name='students'),
    path('api/mentors/', views.getAllMentors, name='mentors'),
    # ex: /polls/5/results/
    path('api/sections/', views.getAllSections, name='sections'),
    # ex: /polls/5/vote/
    path('api/sections/<section_id>/students', views.getStudents, name='students'),

    path('api/sections/<section_id>/details', views.sectionDetail, name='sectionDetail'),
]