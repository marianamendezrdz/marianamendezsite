from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.

def index(request):
    posts = Posts.objects.all()[:10] #[:10] specifies 10 posts on page
    context = {
        'title': 'Latest Posts',
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id) #gets the post id from teh url
    context = {
    'post': post
    }
    return render(request, 'posts/details.html', context)
