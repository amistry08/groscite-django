from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


# class Client(User):
#     AREA = [
#     ('IN', 'India'),
#     ('AR', 'Argentina'),
#     ('CA', 'Canada'),
#     ('PR', 'Portugal'),]
#     firstName = models.CharField(max_length=100,null=True, blank=True)
#     lastName = models.CharField(max_length=100,null=True, blank=True)
#     emailID = models.EmailField(max_length=100,null=True, blank=True)
#     subscription = models.BooleanField(default=False)
#     # location = models.CharField(max_length=2, choices=AREA, default='IN')
#
# class YTVideo(models.Model):
#     title = models.CharField(max_length = 200)
#     description = models.TextField(max_length=500)
#     dateCreated = models.DateTimeField(auto_now_add=True)
#     likes = models.PositiveIntegerField(default=0)
#     url = models.URLField(default='')
#     totalViews = models.PositiveIntegerField(null=True, blank=True)
#     client = models.ForeignKey(Client,on_delete=models.CASCADE)
#
# class Channel(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField(max_length=500)
#
#     def __str__(self):
#         return self.name
#
# class Comment(models.Model):
#     text = models.TextField(max_length=500)
#     dateCreated = models.DateTimeField(auto_now_add=True)
#     video = models.ForeignKey(YTVideo, on_delete=models.CASCADE, related_name='YTVideo')
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    interested = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    # save method is being overridden to check if the value of stock is equal to 0
    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.available = False
        super().save(*args, **kwargs)

    # Restock the Item
    def top_up(self):
        self.stock += 200


class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'WATERLOO'), ]
    # fullname = models.CharField(max_length=50, null=True, blank=True)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='WD')
    interested_in = models.ManyToManyField(Type)
    phoneNumber = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = "Client"


class OrderItem(models.Model):
    itemServing = models.ForeignKey(Item, on_delete=models.CASCADE)
    clientServing = models.ForeignKey(Client, related_name='client', on_delete=models.CASCADE)
    totalItemsOrder = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Placed'),
        (2, 'Shipped'),
        (3, 'Delivered'),
    ]
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clientServing.username

    def total_price(self):
        return self.itemServing.price * self.totalItemsOrder


class Description(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
