from rest_framework import serializers
from .models import Course, Topic, Event, Material, Period, Teacher, Clss, Lesson, Parent, Student, Attendance, Salary, Fee

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "course"]

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "topic", "details"]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["event", "day", "hour"]
        

class MaterialSerializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField()
    topic_id = serializers.IntegerField()
    class Meta:
        model = Material
        fields = ['topic', 'topic_id', 'material', 'event_link']

class PeriodSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    class Meta:
        model = Period
        fields = ['course', 'period']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'gender', 'adress', 'phone', 'email', 'photo', 'salary']

class ClssSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    course_id = serializers.IntegerField()
    period = serializers.StringRelatedField()
    period_id = serializers.IntegerField()
    class Meta:
        model = Clss
        fields = ['course', 'course_id', 'period', 'period_id', 'clss']

class LessonSerializer(serializers.ModelSerializer):
    clss = serializers.StringRelatedField()
    clss_id = serializers.IntegerField()
    topic = serializers.StringRelatedField()
    topic_id = serializers.IntegerField()
    event = serializers.StringRelatedField()
    event_id = serializers.IntegerField()
    teacher = serializers.StringRelatedField()
    teacher_id = serializers.IntegerField()
    material = serializers.StringRelatedField()
    material_id = serializers.IntegerField()
    class Meta:
        model = Lesson
        fields = ['clss', 'clss_id', 'topic', 'topic_id', 'event', 'event_id', 'teacher', 'teacher_id', 'material', 'material_id']

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ["first_name", "last_name", "gender", "adress", "phone", "email", "photo", "register_date", "is_active"]

class StudentSerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField()
    parent_id = serializers.IntegerField()
    course = serializers.StringRelatedField()
    course_id = serializers.IntegerField()
    period = serializers.StringRelatedField()
    period_id = serializers.IntegerField()
    clss = serializers.StringRelatedField()
    clss_id = serializers.IntegerField()
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "gender", "birth_date", "adress", "phone", "email", "parent", "parent_id", "course", "course_id", "period", "period_id", "clss", "clss_id", "photo", "start_date", "end_date", "fee", "is_active"]

class AttendanceSerializer(serializers.ModelSerializer):
    clss = serializers.StringRelatedField()
    clss_id = serializers.IntegerField()
    lesson = serializers.StringRelatedField()
    lesson_id = serializers.IntegerField()
    students = StudentSerializer(many=True, read_only=True)
    class Meta:
        model = Attendance
        fields = ['clss', 'clss_id', 'lesson', 'lesson_id', 'student', 'date', 'status', 'students']

class SalarySerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()
    teacher_id = serializers.IntegerField()
    # salary = serializers.StringRelatedField()
    # salary_id = serializers.IntegerField()
    class Meta:
        model = Salary
        fields = ['id', 'teacher', 'teacher_id', 'due_date', 'is_paid']

class FeeSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    student_id = serializers.IntegerField()
    class Meta:
        model = Fee
        fields = ['id', 'student', 'student_id', 'due_date', 'is_paid']