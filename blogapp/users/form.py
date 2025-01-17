from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


# create, update 기능은 form 사용이 기능 구현하는데 더 편함
class UserForm(UserCreationForm):
    # UserCreationForm : 비밀번호,비밀번호 확인하는 기능 포함됨
    class Meta:
        model = User
        fields = ["email", "name", "gender"]
