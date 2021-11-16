from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.http import request

# Create your models here.

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return 'message from '+self.name

class Feedback(models.Model):
    timeStamp=models.DateTimeField(default=now)
    rating=models.IntegerField(default=4)
    userfeedback=models.TextField(default="no feedback yet")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return " by " + self.user.username

