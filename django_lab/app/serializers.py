
from rest_framework import serializers
from app.models import User, Student, Mentor, Section, Course, Attendance


class MentorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mentor
        fields=['course']

class AttendanceSerializer(serializers.Serializer):
    user_type = serializers.CharField(max_length=2)

    def create(self, validated_data):
        return Attendance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.save()
        return instance

class SectionSerializer(serializers.Serializer):
    student_in_section = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    mentor=MentorSerializer(many=False)
    capacity = serializers.IntegerField()
    special = serializers.BooleanField(default=False)
    name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Section.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.student_in_section = validated_data.get('student_in_section', instance.student_in_section)
        instance.mentor = validated_data.get('mentor', instance.mentor)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.special = validated_data.get('special', instance.special)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class StudentSerializer(serializers.Serializer):
    sectionname = SectionSerializer(many=True)
    attendance = AttendanceSerializer(many=True)
    course = serializers.CharField(max_length=200)
    banned = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.section = validated_data.get('section_name', instance.section_name)
        instance.banned = validated_data.get('banned', instance.banned)
        instance.save()
        return instance

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    mentor=MentorSerializer(many=True)
    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.course = validated_data.get('course', instance.course)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    student = StudentSerializer(many=True)
    mentor = MentorSerializer(many=True)
    username= serializers.CharField()
    email= serializers.CharField()
    first_name= serializers.CharField()
    last_name= serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.student = validated_data.get('student', instance.student)
        instance.mentor = validated_data.get('mentor', instance.mentor)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['student', 'mentor', 'username', 'email', 'first_name', 'last_name']

    
