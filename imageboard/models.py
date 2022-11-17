from django.db import models


# Create your models here.
class Post(models.Model):
    contents = models.TextField(max_length=200)
    image_link = models.URLField(max_length=50)
    date_posted = models.DateTimeField()

