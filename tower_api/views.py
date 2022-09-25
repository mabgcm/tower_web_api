from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Course, Topic, Event, Material, Period, Teacher, Clss, Lesson, Parent, Student, Attendance, Salary, Fee
from .serializers import CourseSerializer, TopicSerializer, EventSerializer, MaterialSerializer, PeriodSerializer, TeacherSerializer, ClssSerializer, LessonSerializer, ParentSerializer, StudentSerializer, AttendanceSerializer, SalarySerializer, FeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def home(request):
    return HttpResponse('<h1>API Page</h1>')

@api_view(['GET', 'POST'])
def tower_api(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Course {serializer.validated_data.get('course')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def tower_api_get_update_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Course {course.course} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = CourseSerializer(course, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Course {course.course} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course.delete()
        data = {
            "message": f"Course {course.course} deleted successfully"
        }
        return Response(data)

# Topic view
@api_view(['GET', 'POST'])
def topic_api(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Topic saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def topic_api_get_update_delete(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == 'GET':
        serializer = TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Topic {topic.topic} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = TopicSerializer(topic, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Topic {topic.topic} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        topic.delete()
        data = {
            "message": f"Topic {topic.topic} deleted successfully"
        }
        return Response(data)

# Event view
@api_view(['GET', 'POST'])
def event_api(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Event saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def event_api_get_update_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Event {event.event} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = EventSerializer(event, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Event {event.event} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        event.delete()
        data = {
            "message": f"Event {event.event} deleted successfully"
        }
        return Response(data)

# Material view
@api_view(['GET', 'POST'])
def material_api(request):
    if request.method == 'GET':
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Material saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def material_api_get_update_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'GET':
        serializer = MaterialSerializer(material)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Material {material.material} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = MaterialSerializer(material, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Material {material.material} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        material.delete()
        data = {
            "message": f"Material {material.material} deleted successfully"
        }
        return Response(data)

# Period view
@api_view(['GET', 'POST'])
def period_api(request):
    if request.method == 'GET':
        periods = Period.objects.all()
        serializer = PeriodSerializer(periods, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Period saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def period_api_get_update_delete(request, pk):
    period = get_object_or_404(Period, pk=pk)
    if request.method == 'GET':
        serializer = PeriodSerializer(period)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PeriodSerializer(period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Period {period.period} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = PeriodSerializer(period, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Period {period.period} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        period.delete()
        data = {
            "message": f"Period {period.period} deleted successfully"
        }
        return Response(data)

# Teacher view
@api_view(['GET', 'POST'])
def teacher_api(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Teacher saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def teacher_api_get_update_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Teacher {teacher.first_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = TeacherSerializer(teacher, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Teacher {teacher.first_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        teacher.delete()
        data = {
            "message": f"Teacher {teacher.first_name} deleted successfully"
        }
        return Response(data)

# Clss view
@api_view(['GET', 'POST'])
def clss_api(request):
    if request.method == 'GET':
        clsss = Clss.objects.all()
        serializer = ClssSerializer(clsss, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClssSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Class saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def clss_api_get_update_delete(request, pk):
    clss = get_object_or_404(Clss, pk=pk)
    if request.method == 'GET':
        serializer = ClssSerializer(clss)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ClssSerializer(clss, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Class {clss.clss} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = ClssSerializer(clss, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Class {clss.clss} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        clss.delete()
        data = {
            "message": f"Class {clss.clss} deleted successfully"
        }
        return Response(data)

# Lesson view
@api_view(['GET', 'POST'])
def lesson_api(request):
    if request.method == 'GET':
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Lesson saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def lesson_api_get_update_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'GET':
        serializer = LessonSerializer(lesson)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = LessonSerializer(lesson, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Lesson {lesson.topic}/{lesson.event.day} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = LessonSerializer(lesson, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Lesson {lesson.topic}/{lesson.event.day} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lesson.delete()
        data = {
            "message": f"Lesson {lesson.topic}/{lesson.event.day} deleted successfully"
        }
        return Response(data)

# Parent view
@api_view(['GET', 'POST'])
def parent_api(request):
    if request.method == 'GET':
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Parent saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def parent_api_get_update_delete(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    if request.method == 'GET':
        serializer = ParentSerializer(parent)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ParentSerializer(parent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Parent {parent.first_name} {parent.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = ParentSerializer(parent, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Parent {parent.first_name} {parent.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        parent.delete()
        data = {
            "message": f"Parent {parent.first_name} {parent.last_name} deleted successfully"
        }
        return Response(data)

# Student view
@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.first_name} {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.first_name} {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.first_name} {student.last_name} deleted successfully"
        }
        return Response(data)

# Attendance view
@api_view(['GET', 'POST'])
def attendance_api(request):
    if request.method == 'GET':
        attendances = Attendance.objects.all()
        serializer = AttendanceSerializer(attendances, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Attendance saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def attendance_api_get_update_delete(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'GET':
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Attendance {attendance.clss}/{attendance.date} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = AttendanceSerializer(attendance, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Attendance {attendance.clss}/{attendance.date} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        attendance.delete()
        data = {
            "message": f"Attendance {attendance.clss}/{attendance.date} deleted successfully"
        }
        return Response(data)

# Salary view
@api_view(['GET', 'POST'])
def salary_api(request):
    if request.method == 'GET':
        salaries = Salary.objects.all()
        serializer = SalarySerializer(salaries, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SalarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Salary saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def salary_api_get_update_delete(request, pk):
    salary = get_object_or_404(Salary, pk=pk)
    if request.method == 'GET':
        serializer = SalarySerializer(salary)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SalarySerializer(salary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Salary {salary}/{salary.due_date} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = SalarySerializer(salary, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Salary {salary}/{salary.due_date} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        salary.delete()
        data = {
            "message": f"Salary {salary}/{salary.due_date} deleted successfully"
        }
        return Response(data)

# Fee view
@api_view(['GET', 'POST'])
def fee_api(request):
    if request.method == 'GET':
        fees = Fee.objects.all()
        serializer = FeeSerializer(fees, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Fee saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def fee_api_get_update_delete(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    if request.method == 'GET':
        serializer = FeeSerializer(fee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = FeeSerializer(fee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Fee {fee.student}/{fee.due_date} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = FeeSerializer(fee, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Fee {fee.student}/{fee.due_date} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fee.delete()
        data = {
            "message": f"Fee {fee.student}/{fee.due_date} deleted successfully"
        }
        return Response(data)
