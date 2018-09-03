from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

# 6255e4e495c6100fffa1a2a81497f6c5bb4910aa