- Get the total number of active students in CSM 1290
    -Student.objects.filter(active=True).count()
    -1290
- Get the total number of attendances with blank presences (i.e. the mentor did not fill anything out for the attendance) 
    -Attendance.objects.filter(presence="").count()
    -4367
- Get the total number of sections with nonzero capacity (capacity ≠ 0) 
    -Section.objects.exclude(capacity=0).count()
    -302
- Get the total number of mentors with sections for CS61B
    -Mentor.objects.filter(course__name="CS61B").count()
    -65
- Get the total number of unexcused absences among all students in CS70 
    -Attendance.objects.filter(presence="UN").filter(student__course__name="CS70").count()
    -259




- Get the total number of active students enrolled in CS61A
    -Student.objects.filter(course__name="CS61A").filter(active=True).count()
    -364
- Get the number of sections with zoom links that contain a password
    -Section.objects.filter(spacetimes__location__contains="zoom").count()
    -44
- Get the total number of attendance objects for dates between 2/1/2022 and 3/1/2022 (inclusive) 
    -start_date = datetime.date(2022,2,1)
    -end_date = datetime.date(2022,3,1)
    -Attendance.objects.filter(sectionOccurrence__date__range=(start_date,end_date)).count()
    -5472
- Challenge: Get the total number of students who have attended at least one section between 2/1/2022 and 3/1/2022 (inclusive) 
    -Attendance.objects.order_by('student').filter(presence="PR").filter(sectionOccurrence__date__range=(start_date,end_date)).distinct('student').count()
    -1287



- Get the total number of users with two or more student profiles 
    - User.objects.annotate(student_count=Count('student')).filter(student_count__gt=1).count()
    - 259
- Get the number of sections with less than 3 students enrolled 
    - Section.objects.annotate(student_count=Count('students')).filter(student_count__lt=3).count()
    - 21



- Get the total number of sections with full capacity  
    - Section.objects.annotate(student_count=Count('students')).filter(student_count=F("capacity")).count()
    - 123
- Get the total number of active students who have at least two unexcused absences between 1/1/2022 and 5/1/2022    
    - Student.objects.filter(Q(active=True),Q(attendance__presence="UN"), Q(attendance__sectionOccurrence__date__range=(start_date,end_date))).annotate(attendance_count=Count('attendance')).filter(attendance_count__gt=1).count()
    - 256
- Get the total number of students who have attended at least one section between 2/1/2022 and 3/1/2022 (inclusive) 
    - 1287
    - Using annotate: Student.objects.filter(Q(attendance__presence="PR"),Q(attendance__sectionOccurrence__date__range=(start_date,end_date))).annotate(attendance_count=Count('attendance')).filter(attendance_count__gt=0).count()
    - Without annotate: Student.objects.annotate(attend=Exists(Attendance.objects.filter(Q(student=OuterRef('pk')),Q(presence="PR"),Q(sectionOccurrence__date__range=(start_date,end_date))))).filter(attend=True).count()