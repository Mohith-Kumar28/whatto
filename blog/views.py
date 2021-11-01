from django.http import response
from django.shortcuts import render,HttpResponse, redirect
from blog.models import Post,BlogComment
from django.contrib import messages

# Create your views here.

def bloghome(request):
    allposts=Post.objects.all()
    # print (allposts)
    context={'allposts':allposts}
    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    # return HttpResponse(f'this is blogpost,,{slug}')

    # this is the place where i used slug as unique identifier, later may change to s.no
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments':comments, 'user':request.user}
    return render(request,'blog/blogpost.html',context)


def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)

        comment= BlogComment(comment=comment,user=user, post=post)
        comment.save()
        messages.success(request,"comment uploaded")
    return redirect(f"/blog/{post.slug}") 


def userPost(request):
    if request.method=="POST":
        title=request.POST.get("title")
        slug=request.POST.get("slug")
        content=request.POST.get("content")
        author=request.user

        post= Post(title=title,slug=slug, content=content,author=author)
        post.save()
        messages.success(request,"comment uploaded")
    return redirect(f"/blog/{post.slug}") 
