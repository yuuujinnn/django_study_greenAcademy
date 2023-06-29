from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# UserCreationForm을 상속받은 UserForm 정의함
class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta: # 중첩 클래스
        model = User
        fields = ('username', 'email')  # 튜플 구조