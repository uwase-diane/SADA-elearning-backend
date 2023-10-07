from django.shortcuts import render
from .models import Course

def home(request):
    context={}
    return render(request, "onlineApp/Homepage.html", context)


def all_courses(request):
    courses = Course.objects.all()
    context={"courses": courses}
    return render(request, 'onlineApp/Homepage.html', context)


def course_details(request):
    course = Course.objects.filter(id=id)
    context = {"course":course}
    return render(request, "onlineApp/Homepage.html", context)


# def enroll_course(request):

#     return render "Homepage.html"