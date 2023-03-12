from django.contrib import admin
from django.db import models
from .models import YTClient, YTVideo, Channel, Comment

# Register your models here.

admin.site.register(YTClient)
admin.site.register(YTVideo)
admin.site.register(Channel)
admin.site.register(Comment)