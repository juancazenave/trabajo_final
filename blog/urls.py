from django.urls import path

from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('homepage/', homepage, name='homepage'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('create-post/', create_post, name='create_post')
]