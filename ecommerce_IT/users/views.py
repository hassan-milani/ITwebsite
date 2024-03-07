from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm
from .decorators import *
from main.models import Client



# Create your views here.

@unauthanticated_user
def registerORlogin(request):
    form = CreateUserForm()
    if request.method == 'POST' and 'loginbtn' not in request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            Client.objects.create(c_name=username, c_email=f'{username}@gmail.com',c_phone=111111)
            return redirect('register')
        else:
            form = CreateUserForm()
            messages.error(request, f'check the information you have entered!')
            
    if request.method == 'POST' and 'loginbtn' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'اسم المستخدم أو كلمة المرور خطأ')
    return render(request, "users/register.html", {'form':form})




def logoutUser(request):
    logout(request)
    return redirect('register')





