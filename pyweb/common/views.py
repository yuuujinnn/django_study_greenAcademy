from django.shortcuts import render, redirect
from common.forms import UserForm

from django.contrib.auth import authenticate, login


# 회원 가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST) # 데이터가 입력된 폼
        if form.is_valid():
            form.save() # 회원 가입 db에 저장
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user) #자동 로그인
            return redirect('/') #index 페이지로 이동
    else:
        form = UserForm() #빈폼 생성
    context = {'form': form}
    return render(request, 'common/signup.html', context)
