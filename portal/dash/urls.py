from django.urls import URLPattern
from . import views
from django.urls import path

app_name = 'dash'

urlpatterns =[
    path('std_signup/', views.std_signup, name='create_student'),
    path('edu_signup/', views.edu_signup, name='create_educator'),
    path('std_login/', views.login_std, name='login_student'),
    path('edu_login/', views.login_edu, name='login_educator'),
    path('add_course/', views.add_course, name='add_course'),
    path('list_course/', views.list_course, name='list_course'),
    path('course/<int:id>/', views.list_course_detail, name = 'course details'),
    path('enroll/<int:id>/', views.enroll, name = "Enroll Student"),
    path('show_students/<int:id>/', views.view_enrolled_user, name = "Enrolled Students"),
]