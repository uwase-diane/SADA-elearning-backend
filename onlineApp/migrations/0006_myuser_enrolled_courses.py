# Generated by Django 4.2.6 on 2023-10-12 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineApp', '0005_myuser_image_alter_myuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='enrolled_courses',
            field=models.ManyToManyField(to='onlineApp.course'),
        ),
    ]