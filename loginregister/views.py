from django.shortcuts import render
from .forms import UserForm
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                return JsonResponse({'message':'用户名已存在'},status=400)
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({'message':'注册成功'},status=201)
        else:
            return JsonResponse({'message':'验证码错误'},status=400)
    else:
        form = UserForm()
    return render(request, 'loginRegister/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                return JsonResponse({'message':'登录成功'},status=200)
            else:
                return JsonResponse({'message':'用户名或密码错误'},status=400)
        else:
            return JsonResponse({'message':'验证码错误'},status=400)
    else:
        form = UserForm()# 如果是 GET 请求，返回空表单
    return render(request,'loginregister/login.html',{'form':form})