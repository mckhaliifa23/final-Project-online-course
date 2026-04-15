from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Course related URLs
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

    # Exam submission URLs
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/result/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),

    # User submission history
    path('my-submissions/', views.my_submissions, name='my_submissions'),
]
