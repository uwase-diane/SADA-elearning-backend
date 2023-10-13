
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
        fields = ['email','firstName','lastName','password']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def save(self):
        user =  MyUser(email=self.validated_data['email'],firstName = self.validated_data['firstName'],lastName = self.validated_data['lastName'])
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