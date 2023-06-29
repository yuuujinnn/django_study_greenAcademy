from django.shortcuts import render, redirect
from .forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)   # 폼에 입력된 데이터를 넘겨 받음
        if form.is_valid():
            form.save() # db 저장
            return redirect('/')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/signup.html', context)
