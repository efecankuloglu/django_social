from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Post, User


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":75}), label=False)
    class Meta:
        model = Post
        fields = ["content"]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}