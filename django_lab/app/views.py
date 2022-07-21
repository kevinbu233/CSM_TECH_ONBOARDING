from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from app.models import Mentor, User, Student, Section
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from app.models import User
from app.serializers import UserSerializer, SectionSerializer, StudentSerializer, MentorSerializer

# - `/api/users/`
#     - `GET`: Return all users in the database
# - `/api/sections/`
#     - `GET`: Return all sections in the database
# - `/api/sections/<section_id>/students`
#     - `GET`: Return all students currently enrolled in the section
# - `/api/sections/<section_id>/details`
#     - `GET`: Get the details about a single section (i.e. capacity and description)
#     - `POST`: Update the section details (i.e. capacity and description, if specified; if not specified, the field should not be touched)

# def index():
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

@api_view(['GET', 'POST'])
def getAllUsers(request):
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def getAllSections(request):
    if request.method == 'GET':
        snippets = Section.objects.all()
        serializer = SectionSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def sectionDetail(request, section_id):
    try:
        section = Section.objects.get(pk=section_id)
    except Section.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SectionSerializer(section)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SectionSerializer(section, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        section.delete()
        return HttpResponse(status=204)

@api_view(['GET',])
def getStudents(request, section_id):
    try:
        section = Section.objects.get(pk=section_id)
    except Section.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        students = Student.objects.filter(sectionname=section_id)
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'POST'])
def getAllStudents(request):
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def getAllMentors(request):
    if request.method == 'GET':
        snippets = Mentor.objects.all()
        serializer = MentorSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MentorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



