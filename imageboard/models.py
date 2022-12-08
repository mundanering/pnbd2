from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField(max_length=200)
    image_link = models.ImageField(null=True, blank=True, upload_to="images/")
    date_posted = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    likes = models.ManyToManyField(User, blank=True, through="Like")

    def get_absolute_url(self):
        return reverse("home")


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_negative = models.BooleanField(default=False)
