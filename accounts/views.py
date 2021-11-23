from django.contrib.auth.models import User,auth
from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        print("user created")
        return redirect('/')
    else:
        return render(request,'register.html')








def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid details")


    else:

        return render(request,"login.html")



def logout(request):
    auth.logout(request)
    return redirect('/')