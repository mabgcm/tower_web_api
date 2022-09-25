from django.db import models

gender = [('F', 'female'), ('M', 'male')]
# Class Model:
class Course(models.Model):
    STARTERS = 'ST'
    MOVERS = 'MV'
    FLYERS = 'FL'
    KET = 'KT'
    PET = 'PT'
    FCE = 'FC'
    COURSE_CHOICES = [
        (STARTERS, 'Starters'),
        (MOVERS, 'Movers'),
        (FLYERS, 'Flyers'),
        (KET, 'KET'),
        (PET, 'PET'),
        (FCE, 'FCE'),
    ]
    course = models.CharField(
        max_length=2,
        choices=COURSE_CHOICES,
        default=STARTERS,
    )

    def __str__(self):
        return self.course

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=gender, default='male')
    adress = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    photo = models.ImageField(upload_to='profile_pics/', blank=True)
    apply_date = models.DateField(auto_now_add=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Topic Model:
class Topic(models.Model):
    topic = models.CharField(max_length=250)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.topic
    
# Lesson session model:
class Event(models.Model):
    event = models.CharField(max_length=50)
    day = models.DateField()
    hour = models.TimeField()

    def __str__(self):
        return self.event

# Lesson Material Model:
class Material(models.Model):
    topic = models.ForeignKey(Topic, related_name='materials', on_delete=models.CASCADE, blank=True, null=True)
    material = models.URLField(max_length=200, blank=True, null=True)
    event_link = models.URLField(max_length=200, blank=True, null=True)

class Period(models.Model):
    course = models.ForeignKey(Course, related_name='periods', on_delete=models.CASCADE)
    period = models.CharField(max_length=15)

    def __str__(self):
        return self.period

class Clss(models.Model):
    course = models.ForeignKey(Course, related_name='clss', on_delete=models.CASCADE)
    period = models.ForeignKey(Period, related_name='clss', on_delete=models.CASCADE)
    clss = models.CharField(max_length=15)

    def __str__(self):
        return self.clss

class Lesson(models.Model):
    clss = models.ForeignKey(Clss, related_name='lessons', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name='lessons', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='lessons', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='lessons', on_delete=models.CASCADE)
    material = models.ForeignKey(Material, related_name='lessons', on_delete=models.CASCADE)

class Parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=gender, default='male')
    adress = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    photo = models.ImageField(upload_to='profile_pics/', blank=True)
    register_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=gender, default='male')
    birth_date = models.DateField(auto_now_add=False, auto_now=False)
    adress = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    parent = models.ForeignKey(Parent, related_name='students', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='students', null=True, blank=True, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, related_name='students', null=True, blank=True, on_delete=models.CASCADE)
    clss = models.ForeignKey(Clss, related_name='students', null=True, blank=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    enroll_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    fee = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Attendance(models.Model):
    PRESENT = 'PR'
    ABSENT = 'AB'
    SICK = 'SK'
    LEAVE = 'LV'
    STATUS_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
        (SICK, 'Sick'),
        (LEAVE, 'Leave'),
    ]
    clss = models.ForeignKey(Clss, related_name='attendance', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='attendance', on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    date = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PRESENT,
    )

    def __str__(self):
        return f'{self.clss}/{self.date}'

class Salary(models.Model):
        # salary = models.ForeignKey(Teacher, related_name='salaries', on_delete=models.CASCADE)
        teacher = models.ForeignKey(Teacher, related_name='teachers', on_delete=models.CASCADE)
        due_date = models.DateField()
        is_paid = models.BooleanField(default=False)

        def __str__(self):
            return f'{self.teacher}/{self.due_date}'

class Fee(models.Model):
        student = models.ForeignKey(Student, related_name='students', on_delete=models.CASCADE)
        due_date = models.DateField()
        is_paid = models.BooleanField(default=False)

        def __str__(self):
            return f'{self.student}/{self.due_date}'
