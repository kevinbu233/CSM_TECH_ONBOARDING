from http.client import HTTPResponse

from app.models import Mentor, User, Student, Section
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import User
from app.serializers import UserSerializer, SectionSerializer, StudentSerializer, MentorSerializer


@api_view(['GET', 'POST'])
def getAllUsers(request):
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def getAllSections(request):
    if request.method == 'GET':
        snippets = Section.objects.all()
        serializer = SectionSerializer(snippets, many=True)
        return Response(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sectionDetail(request, section_id):
    try:
        section = Section.objects.get(pk=section_id)
    except Section.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = SectionSerializer(section)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        section.delete()
        return Response(status=204)

@api_view(['GET',])
def getStudents(request, section_id):
    try:
        section = Section.objects.get(pk=section_id)
    except Section.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        students = Student.objects.filter(sectionname=section_id)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def getAllStudents(request):
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def getAllMentors(request):
    if request.method == 'GET':
        snippets = Mentor.objects.all()
        serializer = MentorSerializer(snippets, many=True)
        return Response(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



