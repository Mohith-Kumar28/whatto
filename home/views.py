from django.db.models import query
from django.http import request
from django.shortcuts import redirect, render,HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'home/home.html')

def contact(request):
    # messages.success(request,"you have successfully entered contact page")
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request,'home/contact.html')
    
def about(request):
   return render(request,'home/about.html')

def search(request):
   query= request.GET['query']
   if len(query)>70 :
       allposts = Post.objects.none()
   else:   
       allpostsTitle=Post.objects.filter(title__icontains=query)
       allpostsContent=Post.objects.filter(content__icontains=query)
       allposts=allpostsTitle.union(allpostsContent)
   if allposts.count() == 0:
       messages.warning(request,"No search results found.")
        #  print("too long")

   params={'allposts':allposts,'query':query}
   return render(request,'home/search.html',params)

def handleSignup(request):
    if request.method == 'POST':
        #Getting post parameters from signup form
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)>10:
            messages.error(request,"hello, Your user name can not exceed 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,"hello, Your username can only contain letters and numbers ")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request,"hello, Your Passwords do not match")
            return redirect('home')



        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request,"hello " + myuser.username + " ,your account is created")
        return redirect('home')  
    else:
        return HttpResponse('404-not allowed, you can only come chere through signup form')

def handlelogin(request):
    if request.method == 'POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"hello, " + user.username + " you are logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('home')

    return HttpResponse('404-not found, u can come here only through login form')
        
def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')