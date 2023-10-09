from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='')

    # string representation - in this case we will return the title
    def __str__(self):
        return self.title


