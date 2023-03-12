import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import Type, Item, Client, OrderItem
from django.shortcuts import get_object_or_404, render
from django.views import View
import calendar


# Create your views here.
'''
def index(request):
    type_list = Type.objects.all().order_by('id')
    item_list = Item.objects.all().order_by('-price')[:10]
    response = HttpResponse()
    heading1 = '<p>' + 'Different Items sorted with Price: ' + '</p>'
    response.write(heading1)
    for items in item_list:
        para = '<p>' + str(items.name) + ': ' + str(items.price) + '</p>'
        response.write(para)
    return response
'''

today = datetime.datetime.now()
year = today.year
month = today.month


def index(request):
    # Yes, The context is passed, which is type_List
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})


def detail(request, type_no):
    obj = get_object_or_404(Item, pk=type_no)
    item_list = Item.objects.filter(type=type_no)
    # Yes, The context is passed, which is item_list
    return render(request, 'myapp1/detail0.html', {'item_list': item_list})


'''
def about(request, year, month):
    response = HttpResponse()
    month_name = calendar.month_name[month]
    heading1 = '<p>' + 'This is an Online Grocery Store: - ' + str(month_name) + ' ' + str(year) + '</p>'
    response.write(heading1)
    return response
'''


def about(request):
    # Yes, The context is passed, which is time
    return render(request, 'myapp1/about0.html', {'time': today.strftime("%B %d, %Y")})


# Class-Oriented View(CBV)
class OrderHistory(View):  # Extended View Class to OrderHistory (FBV does not require this)
    def get(self, request, user_id):  # using get HTTP method (FBV needs conditional branching)
        response = HttpResponse()
        client = Client.objects.get(id=user_id)
        heading1 = '<p>' + 'Order History of ' + client.username + '</p>'
        response.write(heading1)

        orders = OrderItem.objects.filter(clientServing=user_id)

        for items in orders:
            para = '<p>Item: ' + str(items.itemServing.name) \
                   + '<br>Quantity: ' + str(items.totalItemsOrder) \
                   + '<br>Total Price: $' + str(items.total_price()) \
                   + '<br>Status: ' + str(items.STATUS_CHOICES[items.status][1]) + '<br><br></p>'
            response.write(para)

        return response


def items(request):
    item_list = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'item_list': item_list})


def placeorder(request):
    return render(request, 'myapp1/placeorder.html', {})
