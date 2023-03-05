from django.shortcuts import render

from .models import Post
from .forms import *

# Create your views here.
def base(request):
    return render(request, 'blog/base.html')

def homepage(request):
    posts = Post.objects.all()
    return render(request, 'blog/homepage.html', {'posts':posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
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

def erase_post(request, id):
    post_erased = Post.objects.get(id=id)
    post_erased.delete()

    # direcciono a pagina donde indico el Post que se borra
    return render(request, 'blog/erase_post.html', {'post':post_erased})

def edit_post(request, id):
# recibo el nombre del post que voy a modificar
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        # recibo la informacion del HTML (lo que ingresa el usuario)
        miPost = PostFormulario(request.POST)
        print(miPost)
        
        # si pasa la validacion de Django (CharField,TextField, length, etc)
        if miPost.is_valid:
            # el 'cleaned_data' va a limpiar la data que trae el formulario
            infopost = miPost.cleaned_data
            
            # aca voy a definir los campos que quiero o permito editar
            post.title = infopost['title']
            post.intro = infopost['intro']
            post.body = infopost['body']

            # con el save() se graba la info nuevamente en post, con el 'id' que di al principio
            post.save()

            # 
            updated_posts = Post.objects.all()
            contexto = {'posts': updated_posts}

            # Back to HomePage
            return render(request, 'blog/homepage.html', contexto)
    
    else:

        miPost = PostFormulario(initial={'title': post.title, 'intro': post.intro, 'body': post.body})
    
    return render(request, 'blog/edit_post.html', {'mi_post': miPost})
