from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    contents = models.TextField(max_length=200)
    image_link = models.URLField(max_length=50)
    date_posted = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

