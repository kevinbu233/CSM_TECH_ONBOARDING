from django.core.management import BaseCommand
from app.models import User, Student, Mentor, Section, Course

import random

from faker import Faker

NUM_TO_CREATE = 20


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        users = []
        # create users
        for i in range(NUM_TO_CREATE):
            first = fake.first_name()
            last = fake.last_name()
            user = User.objects.create(
                username=f"{first}{last}",
                email=f"{first}{last}@berkeley.edu",
                first_name=first,
                last_name=last,
            )
            users.append(user)

        # create course
        course = Course.objects.create(name="CS70")

        # create mentors
        mentors = []
        potential_students = []
        for i, user in enumerate(users):
            is_mentor = (i == 0 or random.choice([True, False])) and len(mentors) < 3
            if is_mentor:
                mentor = Mentor.objects.create(user=user, course=course)
                mentors.append(mentor)
            else:
                potential_students.append(user)

        # create sections for each mentor
        sections = []
        for mentor in mentors:
            section = Section.objects.create(mentor=mentor, capacity=10)
            sections.append(section)

        # create students
        for user in potential_students:
            section = random.choice(sections)
            Student.objects.create(
                user=user,
                section=section,
                course=section.mentor.course,
                active=random.choice([True, False]),
                banned=False,
            )