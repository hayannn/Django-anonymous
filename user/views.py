from django.shortcuts import render, HttpResponse

# 로그인 함수
def signin(request):
    if request.method == "GET":
        return render(request, 'page/signin.html')

# 회원가입 함수
def signup(request):
    if request.method == "POST":
        return HttpResponse("회원가입 페이지 - POST 요청에 대한 응답입니다.")
    else:
        return render(request, 'page/signup.html')