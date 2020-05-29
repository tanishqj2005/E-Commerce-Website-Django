from django.shortcuts import render
from .models import blogPost
# Create your views here.
from django.http import HttpResponse

def index(request):
    myposts = blogPost.objects.all()
    return render(request, 'blog/index.html',{'myposts':myposts})

def blogpost(request, id):
    myposts = blogPost.objects.all()
    ids = []
    for post in myposts:
        ids.append(post.post_id)
    ids.sort()
    first = ids[0]
    last = ids[-1]
    print(first,last)
    post = blogPost.objects.filter(post_id = id)[0]
    if id == first:
        nextpost = True
        prevpost = False
        nextp=id+1
        prevp=0
    elif id==last:
        nextpost = False
        prevpost = True
        nextp=0
        prevp=id-1
    else:
        nextpost=True
        nextp=id+1
        prevp=id-1
        prevpost=True
    return render(request, 'blog/blogpost.html',
                  {'post':post,'id':id,'nextpost':nextpost,'prevpost':prevpost,'nextp':nextp,'prevp':prevp})

    