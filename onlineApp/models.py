from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)

    description = models.TextField(default='')

    image = models.ImageField(upload_to='images/')

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return None

    # string representation - in this case we will return the title
    def __str__(self):
        return self.course_name

class MyUserManager(BaseUserManager):
    def create_user(self, email, firstName, lastName, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            email=self.normalize_email(email), firstName = firstName, lastName = lastName
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, firstName, lastName, password=None):
        user = self.create_user(
            email,
            password=password,
            firstName= firstName,
            lastName=lastName
           
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class MyUser(AbstractBaseUser):

    email = models.EmailField(max_length=255,unique=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True)
    # school = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    enrolled_courses = models.ManyToManyField(Course)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName','lastName']

    def __str__(self):
        return self.email
        # return f"{self.firstName} {self.lastName}"
    
    def has_perm(self, perm, obj=None):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True 