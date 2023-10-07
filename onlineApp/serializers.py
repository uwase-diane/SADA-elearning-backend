from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        mode = Course
        field = '__all__'