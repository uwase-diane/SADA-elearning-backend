
from rest_framework import serializers
from .models import Course
from .models import MyUser


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('__all__')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password =  serializers.CharField(style={"input_type":"password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['email','first_name','last_name','password']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def save(self):
        user =  MyUser(email=self.validated_data['email'],first_name = self.validated_data['first_name'],last_name = self.validated_data['last_name'])
        password = self.validated_data['password']
       
        user.set_password(password)
        user.save()
        return user


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = MyUser
        fields = ['token']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)    