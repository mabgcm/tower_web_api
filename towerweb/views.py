from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required,user_passes_test
from tower_api import models
from tower_api.models import Clss
from django.db.models import Sum, Count
from datetime import date
from .forms import PeriodForm, ClassForm


def home(request):
    return render(request, 'towerweb/home.html')

def courses(request):
    stperiodscount=models.Period.objects.all().filter(course_id=1).count()
    period = models.Period.objects.all().filter(course_id=1)
    st_period = models.Period.objects.annotate(nstud=Count('students'))
    mydict = {
        'stperiodscount': stperiodscount,
        'period': period,
        'st_period': st_period,
    }
    return render(request, 'towerweb/courses.html', context=mydict)

def classes(request):
    classescount=models.Period.objects.all().count()
    clss = models.Clss.objects.all()
    st_cls = models.Clss.objects.annotate(nstud=Count('students'))
    mydict = {
        'classescount': classescount,
        'clss': clss,
        'st_cls': st_cls,
    }
    return render(request, 'towerweb/classes.html', context=mydict)

def user_login(request):
    login(request)
    return render(request, 'towerweb/adminlogin.html')

# def is_admin(user):
#     return user.groups.filter(name='admin').exists()

# @login_required(login_url='dashboard')
# @user_passes_test(is_admin)
def admindashboard(request):
    coursescount=models.Course.objects.all().count()
    clasescount=models.Clss.objects.all().count()
    teachercount=models.Teacher.objects.all().filter(is_active=True).count()

    lesson = models.Lesson.objects.all()
    # teacher = models.Teacher.objects.all()
    salary = models.Salary.objects.all()
    today = date.today()


    # pendingteachercount=models.Teacher.objects.all().filter(status=False).count()

    studentcount=models.Student.objects.all().filter(is_active=True).count()
    # pendingstudentcount=models.StudentExtra.objects.all().filter(status=False).count()

    teachersalary=models.Teacher.objects.filter(is_active=True).aggregate(Sum('salary'))
    # pendingteachersalary=models.TeacherExtra.objects.filter(status=False).aggregate(Sum('salary'))

    studentfee=models.Student.objects.filter(is_active=True).aggregate(Sum('fee'))
    # pendingstudentfee=models.StudentExtra.objects.filter(status=False).aggregate(Sum('fee'))

    # notice=models.Notice.objects.all()

    #aggregate function return dictionary so fetch data from dictionay
    mydict={
        'coursescount':coursescount,
        'clasescount':clasescount,
        'teachercount':teachercount,
        'lesson': lesson,
        # 'teacher': teacher,
        'salary': salary,
        'today': today,

        # 'pendingteachercount':pendingteachercount,

        'studentcount':studentcount,
        # 'pendingstudentcount':pendingstudentcount,

        'teachersalary':teachersalary['salary__sum'],
        # 'pendingteachersalary':pendingteachersalary['salary__sum'],

        'studentfee':studentfee['fee__sum'],
        # 'pendingstudentfee':pendingstudentfee['fee__sum'],

        # 'notice':notice

    }

    return render(request,'towerweb/admindashboard.html',context=mydict)

def user_logout(request):
    logout(request)
    return redirect('home')

def user_login(request):
    form=AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('admindashboard')
    return render(request, 'towerweb/adminlogin.html', {'form':form})    

def add_period(request):
    form = PeriodForm()
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    context = {
        'form': form
    }
    return render(request, 'towerweb/addperiod.html', context)

def add_class(request):
    form = ClassForm()
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
    context = {
        'form': form
    }
    return render(request, 'towerweb/addclass.html', context)

def update_class(request, id):
    clss = Clss.objects.get(id=id)
    form = ClassForm(instance=clss)
    if request.method =='POST':
        form = ClassForm(request.POST, instance=clss)
        if form.is_valid():
            form.save()
            return redirect('classes')
    context = {
        'form': form,
    }
    return render(request, 'towerweb/updateclass.html', context)