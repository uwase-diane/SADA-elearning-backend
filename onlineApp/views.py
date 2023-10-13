from django import views
from django.shortcuts import render
from .serializers import CourseSerializer
from .models import Course
from rest_framework import generics
from .serializers import RegistrationSerializer,LoginSerializer,EmailVerificationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .utils import get_tokens_for_user
from .backends import EmailBackend
from rest_framework.authtoken.models import Token
import jwt
from django.conf import settings
from .models import MyUser
from functools import wraps
from jwt import DecodeError, ExpiredSignatureError
from .utils import Util, get_tokens_for_user
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse

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


class VerifyEmail(APIView):

    serializer_class = EmailVerificationSerializer
    def get(self, request):
        token = request.GET.get('token')
        # print("show me this ",token)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = MyUser.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            # return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
            resp = """<div style="width:100vw; heigt:100vh; display:flex; flex-direction:column; align-item:center; justify-content:center">
                        <p>Thank you for verifying your email</p>  <a href="http://localhost:3000/login/">You can now login from here!</a></div>"""
            return HttpResponse(resp)
        except jwt.ExpiredSignatureError as e:

            return Response({'error': f'Activation Expired: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as e:
            return Response({'error': f'Invalid token: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

class RegistrationView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = jwt.encode({'user_id': user.id}, settings.SECRET_KEY, algorithm='HS256')
            relative_link = f"http://127.0.0.1:8000/api/verify-email/?token={token}"
            print("token--->", token)
            send_mail(
                '!!VERIFY YOUR ACCOUNT'+ " "+user.firstName,
                f'Thank you for registering! Click here to verify your email: {relative_link}',
                'projetest123@gmail.com',
                [user.email],
                fail_silently=False
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_serializer(self, *args, **kwargs):
        return RegistrationSerializer(*args, **kwargs)


class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'], backend=EmailBackend)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg':'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'error':'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

class EnrollView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
