from django.http import response
from django.shortcuts import render,HttpResponse, redirect
from blog.models import Post,BlogComment
from django.contrib import messages

# Create your views here.

def bloghome(request):
    
    #here i added orderby slug to apply decending order 
  

    allposts=Post.objects.all().order_by('-votes')
    # allposts=Post.objects.all().order_by('-slug')
    # allposts=Post.objects.extra(select={'offset': 'likes - dislikes'}).order_by('offset')
    

    # allposts=Post.objects.all()
    # print (allposts)
    context={'allposts':allposts}
    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    # return HttpResponse(f'this is blogpost,,{slug}')
    
    # this is the place where i used slug as unique identifier, later may change to s.no
    post=Post.objects.filter(slug=slug).first()
    
    
    comments= BlogComment.objects.filter(post=post).order_by('-timestamp')
    context={'post':post, 'comments':comments, 'user':request.user}
    return render(request,'blog/blogpost.html',context)
    

def categoryblogpost(request,category):
    allposts=Post.objects.filter(category=category).order_by('-votes')
    context={'allposts':allposts}
    return render(request,'blog/category.html',context)

def sortcategoryblogpost(request,sort,category):
    if sort=="hightolow":
     allposts=Post.objects.filter(category=category).order_by('-votes')
    if sort=="lowtohigh":
     allposts=Post.objects.filter(category=category).order_by('votes')
    if sort=="newfirst":
     allposts=Post.objects.filter(category=category).order_by('-timeStamp')
    if sort=="oldfirst":
     allposts=Post.objects.filter(category=category).order_by('timeStamp')
    context={'allposts':allposts}
    return render(request,'blog/sort.html',context)

def sortby(request,sort):
    if sort=="hightolow":
     allposts=Post.objects.all().order_by('-votes')
    if sort=="lowtohigh":
     allposts=Post.objects.all().order_by('votes')
    if sort=="newfirst":
     allposts=Post.objects.all().order_by('-timeStamp')
    if sort=="oldfirst":
     allposts=Post.objects.all().order_by('timeStamp')
    context={'allposts':allposts}
    return render(request,'blog/sort.html',context)

def wishlistview(request):
    allposts=Post.objects.filter(wishlist = request.user).order_by('-votes')
    context={'allposts':allposts}
    return render(request,'blog/wishlistview.html',context)


def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(slug=postSno)
        # post=Post.objects.get(sno=postSno)

        comment= BlogComment(comment=comment,user=user, post=post)
        comment.save()
        messages.success(request,"comment uploaded")
    return redirect(f"/blog/{post.slug}") 


def userPost(request):
    if request.method=="POST":
        title=request.POST.get("title")
        category=request.POST.get("category")
        video=request.POST.get("video")
        # slug=request.POST.get("slug")
        # slug=request.slug
        content=request.POST.get("content")
        
        author=request.user
        
        # post= Post(title=title,slug=slug, content=content,author=author)
        post= Post(title=title,content=content,author=author,video=video,category=category)

        post.save()
        messages.success(request,"Post uploaded")
  
    return redirect(f"/blog/{post.slug}") 


# def AddLike(request):
def AddLike(request,slug):
        # totalLikes=request.POST.get("totalLikes")
        post = Post.objects.get(slug=slug)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like: 
            post.likes.add(request.user)
            
        if is_like:
            post.likes.remove(request.user)
        vote=post.likes.count() - post.dislikes.count()    
        # print( vote ) 
        post.votes = vote
        post.save() 
        # print( post.votes ) 
        return redirect(f"/blog/")

def AddDislike(request,slug):
        post = Post.objects.get(slug=slug)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike: 
            post.dislikes.add(request.user)
        
        if is_dislike:
            post.dislikes.remove(request.user)

        vote=post.likes.count() - post.dislikes.count()    
        # print( vote ) 
        post.votes = vote
        post.save() 
        # print( post.votes ) 
        
        return redirect(f"/blog/")
        # if(is_dislike):
        #     active="primary"
        # if(not is_dislike):
        #     active="light"

        # context={'active':active}
        # return render(request,'/blog/',context)

def Addwishlist(request,slug):
        post = Post.objects.get(slug=slug)
        is_wishlist = False

        for wishlist in post.wishlist.all():
            if wishlist == request.user:
                is_wishlist = True
                break

        if not is_wishlist: 
            post.wishlist.add(request.user)
        
        if is_wishlist:
            post.wishlist.remove(request.user)

     
        
        return redirect(f"/blog/")
