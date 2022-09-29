from django.urls import path
from .views import home, admindashboard, user_logout, user_login, courses, add_period, classes, add_class, update_class

urlpatterns = [
    path('', home, name='home'),
    path('admindashboard/', admindashboard, name='admindashboard'),
    path('courses/', courses, name='courses'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('courses/', courses, name='courses'),
    path('classes/', classes, name='classes'),
    path('addperiod/', add_period, name='addperiod'),
    path('addclass/', add_class, name='addclass'),
    path('updateclass/<int:id>', update_class, name='updateclass'),
]