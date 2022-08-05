from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from backend.models import Attendance, User, Section, Student
from backend.serializers import (
    UserSerializer,
    StudentSerializer,
    MentorSerializer,
    SectionSerializer,
    CourseSerializer,
    AttendanceSerializer
)


@api_view(["GET"])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def sections(request):
    sections = Section.objects.all()
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "DELETE"])
def section_students(request, section_id):
    if request.method == "GET":
        section = Section.objects.get(id=section_id)
        students = section.student_set.filter(active=True)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        students = Section.objects.get(id=section_id).student_set.filter(active=True)
        student = students.get(id = request.data.get("value"))
        student.active = False
        student.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(["GET", "POST"])
def section_details(request, section_id):
    """
    GET: Return section details
    POST: Update section details
        - format: { "capacity": int, "description": str }
    """
    if request.method == "GET":
        section = Section.objects.get(id=section_id)
        serializer = SectionSerializer(section)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        section = Section.objects.get(id=section_id)
        capacity = request.data.get("capacity")
        description = request.data.get("description")
        if capacity is not None:
            section.capacity = capacity
        if description is not None:
            section.description = description
        section.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(["GET"])
def student_details(request, student_id):
    """
    GET: Return student details
    """
    if request.method == "GET":
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def attendance_details(request, attendance_id):
    """
    GET: Return student details
    """
    if request.method == "GET":
        attendance = Attendance.objects.get(id=attendance_id)
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        attendance = Attendance.objects.get(id=attendance_id)
        attendance.presence = request.data.get("value")
        attendance.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(["GET"])
def attendance_student(request, student_id):
    """
    GET: Return student details
    """
    if request.method == "GET":
        attendance = Attendance.objects.filter(student_id = student_id)
        serializer = AttendanceSerializer(attendance, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

