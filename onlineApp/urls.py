from django.urls import path
from .views import AllCourses, CourseDetails,RegistrationView,LoginView,VerifyEmail,EnrollView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('all/', AllCourses.as_view()),
    path('course/<int:pk>/', CourseDetails.as_view()),

    # user authentication
    
    path('register/', RegistrationView.as_view(), name='register'),
	path('login/', LoginView.as_view(), name='login'),
	# path('logout/', LogoutView.as_view(), name='logout'),
	# path('user/', UserView.as_view(), name='user'),
    path('verify-email/',VerifyEmail.as_view(), name="VerifyEmail"),
    path('enroll/', EnrollView.as_view(), name='enroll-student'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)