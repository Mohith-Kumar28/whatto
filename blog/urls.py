from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('postComment',views.postComment,name="postComment"),
    
  
    path('userPost',views.userPost,name="userPost"),



    path('', views.bloghome, name='bloghome'),
    path('<int:slug>', views.blogpost, name='home'),
    path('<int:slug>/like', views.AddLike, name='like'),
    path('<int:slug>/Dislike', views.AddDislike, name='Dislike'),
    path('<int:slug>/wishlist', views.Addwishlist, name='wishlist'),

    path('category/<str:category>', views.categoryblogpost, name='category'),
    path('wishlistview/', views.wishlistview, name='wishlistview')
    # path('<str:slug>', views.blogpost, name='home')

]