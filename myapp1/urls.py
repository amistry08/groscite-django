from django.urls import path
from . import views

app_name = 'myapp1'
urlpatterns = [
 path('', views.index, name='index'),
 path('detail/<int:type_no>/', views.detail, name='detail'),
 path('about/', views.about, name='about'),
 path('orderhistory/<int:user_id>/', views.OrderHistory.as_view(), name='order_history'),
 path('items/', views.items, name='items'),
 path('placeorder/', views.placeorder, name='place_order')
]
