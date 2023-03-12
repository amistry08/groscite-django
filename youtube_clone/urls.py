from django.urls import path
from . import views

app_name = 'youtube_clone'
urlpatterns = [
 path('', views.index, name='index'),
 path('detail/<int:video_id>/', views.detail, name='detail'),
 path('channel/<int:channel_id>', views.channel, name='channel'),
 path('about/', views.about, name='about'),
]
