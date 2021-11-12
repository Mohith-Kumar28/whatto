from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('postComment',views.postComment,name="postComment"),
    
  
    path('userPost',views.userPost,name="userPost"),



    path('', views.bloghome, name='bloghome'),
    path('<int:slug>', views.blogpost, name='home'),
    path('<int:slug>/like', views.AddLike, name='like'),
    path('<int:slug>/Dislike', views.AddDislike, name='Dislike')

    # path('<str:slug>', views.blogpost, name='home')

]