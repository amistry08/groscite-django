from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class YTClient(User):
    AREA = [
        ('IN', 'India'),
        ('AR', 'Argentina'),
        ('CA', 'Canada'),
        ('PR', 'Portugal'), ]
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    emailID = models.EmailField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=2, choices=AREA, default='IN')

    class Meta:
        verbose_name = "Client"


class YTVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    dateCreated = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    client = models.ForeignKey(YTClient, on_delete=models.CASCADE)
    totalViews = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Channel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    client = models.ForeignKey(YTClient, on_delete=models.CASCADE)
    subscription = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField(max_length=500)
    dateCreated = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(YTVideo, on_delete=models.CASCADE, related_name='YTVideo')
    client = models.ForeignKey(YTClient, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.username + " - " + self.video.title

