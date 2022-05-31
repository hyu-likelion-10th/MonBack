from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    # request == POST
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'bad_login.html',)
    # 로그인 시키기

    # request == GET
    else:
        return render(request, 'login.html')


    # login html 띄우기

def logout(request):
    auth.logout(request)
    return redirect('main')

