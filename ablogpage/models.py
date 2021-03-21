from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title= models.CharField(max_length=255)
    body=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=255)
    image=models.ImageField(upload_to ="upload/")

    def __str__(self):
        return self.title