from django.shortcuts import render
from .models import YTVideo, Comment, Channel


# Create your views here.


def index(request):
    yt_video = YTVideo.objects.all().order_by('id')
    return render(request, 'youtube/index.html', {"yt_video": yt_video})


def detail(request, video_id):
    video_details = YTVideo.objects.get(id=video_id)
    comments = Comment.objects.filter(video=video_id)
    channel_details = Channel.objects.get(client=video_details.client)
    return render(request, 'youtube/detail.html', {"video_details": video_details, "comments": comments,
                                                   "channel_details": channel_details})


def channel(request, channel_id):
    channel_details = Channel.objects.get(id=channel_id)
    yt_video = YTVideo.objects.filter(client=channel_details.client.id)
    return render(request, 'youtube/channel.html', {"channel_details": channel_details, "yt_video": yt_video})


def about(request):
    message = 'This is a youtube Website, You can watch video here!!'
    return render(request, 'youtube/about.html', {"message": message})

