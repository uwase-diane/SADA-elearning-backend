from django.urls import path
from .views import AllCourses, CourseDetails


urlpatterns = [
    path('all/', AllCourses.as_view()),
    path('course/<int:pk>/', CourseDetails.as_view()),
]