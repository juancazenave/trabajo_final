from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .models import Post
from .forms import *

class PostList(ListView):
    model = Post
    template_name = 'blog/homepage.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class CreatePost(CreateView):
    model = Post
    success_url = 'blog/create_post.html'

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

def edit_post(request, post_id):
# recibo el nombre del post que voy a modificar
    post = Post.objects.get(id=post_id)

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

            # Back to HomePage
            return render(request, 'blog/homepage.html')
    
    else:

        miPost = PostFormulario(initial={'title': post.title, 'intro': post.intro, 'body': post.body})
    
    return render(request, 'blog/edit_post.html', {'miPost': miPost, 'post_id': post_id})

def login_request(request):
    form = AuthenticationForm()

    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            psw = form.cleaned_data.get('password')

            user = authenticate(username=user, password=psw)

            if user is not None:
                login(request, user)
                contexto = {'mensaje': f'Welcome {user}'}
                return render(request, 'blog/homepage.html', contexto)
            else:
                return render(request, 'blog/login.html', {'mensaje': 'Error: User not existing', 'form': form})
        
        else:
            contexto = {'mensaje': 'Error: User or Password Incorrect', 'form': form}
            return render(request, 'blog/login.html', contexto)

    contexto = {'form': form}
    return render(request, 'blog/login.html', contexto)

def register(request):
     
    if request.method == 'POST':
        #  form = UserCreationForm(request.POST)
         form = MyUserCreationForm(request.POST)

         if form.is_valid():
             username = form.cleaned_data['username']
             form.save()
             contexto = {'mensaje': 'User created successfully!'}
             return render(request, 'blog/homepage.html', contexto)
    
    # si el usuario aun no se ha registrado, con el else le damos un formulario vacio
    else:
        # form = UserCreationForm()
        form = MyUserCreationForm()
    
    return render(request, 'blog/register.html', {'form': form})
    

