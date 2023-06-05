from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.

from .models import item
def demo(request):
    obj = item.objects.all()
    return render(request, "index.html",{'item':obj})




def register(request):
    if request.method== 'POST':    #fetching data from form
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']

        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request,'password not matched')
            return redirect('register')
        print('user created')
        return redirect('/')
    return render(request,'register.html')








def login(request):
    if request.method=='POST':
        username=request.POST['name']
        pas=request.POST['password']
        user=auth.authenticate(username=username,password=pas)

        if user is not None:
            auth.login(request,user)
            print('logined')
            return redirect('/')
        else:
            messages.info(request,'Invalid')
            print('login failed')
            return redirect('login')
    return render(request, 'login.html')




def logout(request):
    auth.logout(request)
    return redirect('/')


def form(request):
    return render(request,'form.html')