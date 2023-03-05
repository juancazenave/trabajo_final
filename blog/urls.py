from django.urls import path

from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('homepage/', homepage, name='homepage'),
    path('post/<id>/', post_detail, name='post_detail'),
    path('create-post/', create_post, name='create_post'),
    path('erase-post/<id>/', erase_post, name='erase_post'),
    path('edit-post/<post_id>/', edit_post, name='edit_post')
]