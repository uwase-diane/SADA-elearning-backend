from django.urls import path
from .views import AllCourses, CourseDetails


urlpatterns = [
    path('all/', AllCourses.as_view()),
    path('course/<int:pk>/', CourseDetails.as_view()),

    # user authentication
    
    # path('register/', UserRegistrationView.as_view(), name='register'),
	# path('login/', UserLoginView.as_view(), name='login'),
	# path('logout/', UserLogout.as_view(), name='logout'),
	# path('user/', UserView.as_view(), name='user'),

]