from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group, Permission
from django.utils import timezone

    
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
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        return self.create_user(email, first_name, last_name, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    enrolled_courses = models.ManyToManyField(Course)
    groups = models.ManyToManyField(Group, related_name='my_users')
    user_permissions = models.ManyToManyField(Permission, related_name='my_users')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True