from django.urls import path
from .views import home, admindashboard, user_logout, user_login, courses

urlpatterns = [
    path('', home, name='home'),
    path('admindashboard/', admindashboard, name='admindashboard'),
    path('courses/', courses, name='courses'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]