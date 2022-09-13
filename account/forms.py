from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'age', 'username', 'date_of_birth')

    def clean_password2(self):  #두 비밀번호 입력 일치 확인
        password1 = self.cleaned_data.get("password1")  #cleaned_data = form 안에서 validate 된 후에 데이터가 들어간 변수
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:  #패스워드 1과2가 맞지 않으면 리턴
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    #비밀번호 변경 폼
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'age', 'username', 'date_of_birth',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]