from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from user.models import User

# 로그인 함수
def signin(request):
    if request.method == "GET":
        return render(request, 'page/signin.html')
    
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('board')
        else:
            messages.error(request, "입력값을 확인해주세요.")
            return redirect('signin')

# 회원가입 함수
def signup(request):
    if request.method == "GET":
        return render(request, 'page/signup.html')
    
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        nickname=request.POST['nickname']

        user = User.objects.filter(username=username)
        # exists - 존재하면 True, 존재하지 않으면 False
        if user.exists():
            messages.error(request, "이미 가입한 아이디 입니다.")
            return redirect('signup')
        else:
            new_user = User(
                username=username,
                password=make_password(password),
                nickname=nickname,
            )
            new_user.save()
            login(request, new_user)
            return redirect('board')