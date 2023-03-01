from django.shortcuts import render

from .models import Post
from .forms import *

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

    if request.method == 'POST':
        miFormulario = PostFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            publicacion = Post(title=informacion['title'], intro=informacion['intro'], body=informacion['body'])
            publicacion.save()
            return render(request, 'blog/homepage.html')
    
    else:
        miFormulario = PostFormulario()

    return render(request, 'blog/create_post.html', {"miFormulario": miFormulario})
