from django.urls import path
from .views import home,tower_api, event_api, topic_api, material_api, period_api, teacher_api, clss_api, lesson_api, parent_api, student_api, attendance_api, salary_api, fee_api, tower_api_get_update_delete, topic_api_get_update_delete, event_api_get_update_delete, material_api_get_update_delete, period_api_get_update_delete, teacher_api_get_update_delete, clss_api_get_update_delete, lesson_api_get_update_delete, parent_api_get_update_delete, student_api_get_update_delete, attendance_api_get_update_delete, salary_api_get_update_delete, fee_api_get_update_delete

urlpatterns = [
    path('', home),
    path('course/', tower_api),
    path('topic/', topic_api),
    path('event/', event_api),
    path('material/', material_api),
    path('period/', period_api),
    path('teacher/', teacher_api),
    path('clss/', clss_api),
    path('lesson/', lesson_api),
    path('parent/', parent_api),
    path('student/', student_api),
    path('attendance/', attendance_api),
    path('salary/', salary_api),
    path('fee/', fee_api),
    path('course/<int:pk>/', tower_api_get_update_delete, name ="course"),
    path('topic/<int:pk>/', topic_api_get_update_delete, name = "topic"),
    path('event/<int:pk>/', event_api_get_update_delete, name = "event"),
    path('material/<int:pk>/', material_api_get_update_delete, name = "material"),
    path('period/<int:pk>/', period_api_get_update_delete, name = "period"),
    path('teacher/<int:pk>/', teacher_api_get_update_delete, name = "teacher"),
    path('clss/<int:pk>/', clss_api_get_update_delete, name = "clss"),
    path('lesson/<int:pk>/', lesson_api_get_update_delete, name = "lesson"),
    path('parent/<int:pk>/', parent_api_get_update_delete, name = "parent"),
    path('student/<int:pk>/', student_api_get_update_delete, name = "student"),
    path('attendance/<int:pk>/', attendance_api_get_update_delete, name = "attendance"),
    path('salary/<int:pk>/', salary_api_get_update_delete, name = "salary"),
    path('fee/<int:pk>/', fee_api_get_update_delete, name = "fee"),
]