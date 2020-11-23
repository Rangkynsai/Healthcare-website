from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 33)
    phone_no = models.CharField(max_length = 34)
    email = models.CharField(max_length = 35)
    options = models.CharField(max_length = 36)
    date_1 = models.CharField(max_length = 37)
    time_1 = models.CharField(max_length = 38)

class Medicine(models.Model):
    name = models.CharField(max_length=35)
    mail = models.CharField(max_length=35)
    content = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    content = models.TextField()

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    content = models.TextField()

class Postblog(models.Model):
    date_time = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    content = models.TextField()
    images = models.ImageField(default="default.jpg",upload_to='picture')