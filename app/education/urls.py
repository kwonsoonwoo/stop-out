from django.conf.urls import url
from django.urls import path

from education.views import school_list, school_detail, student_list, student_detail

urlpatterns = [
    path('school/', school_list, name='school-list'),
    path('school/<int:school_id>/', school_detail, name='school-detail'),
    path('student/', student_list, name='student_list'),
    path('student/<int:student_id>/', student_detail, name='student-detail'),
]