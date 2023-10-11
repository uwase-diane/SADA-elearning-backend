from django.shortcuts import render
from .serializers import CourseSerializer
from .models import Course
from rest_framework import generics

# from .views import UserRegister 
def home(request):
    context={}
    return render(request, "onlineApp/Homepage.html", context)


# def Allcourses(request):
#     courses = Course.objects.all()
#     context={"courses": courses}
#     return render(request, 'onlineApp/Homepage.html', context)

class AllCourses(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()




class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

# permission_classes = (permissions.IsAuthenticated,)



