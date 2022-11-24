from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField(max_length=200)
    image_link = models.URLField(max_length=200)
    date_posted = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    likes = models.ManyToManyField(User, blank=True, through="Like")


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_negative = models.BooleanField(default=False)
