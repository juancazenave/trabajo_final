from django.shortcuts import render

from .models import Post

# Create your views here.
def base(request):
    return render(request, 'blog/base.html')

def homepage(request):
    posts = Post.objects.all()
    return render(request, 'blog/homepage.html', {'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post})

def create_post(request):
    return render(request, 'blog/create_post.html')
