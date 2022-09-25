from django.urls import path
from .views import home, admindashboard, user_logout, user_login

urlpatterns = [
    path('', home, name='home'),
    path('admindashboard/', admindashboard, name='admindashboard'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]