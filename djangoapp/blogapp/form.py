from django import forms
from .models import article
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm


class createForm(forms.ModelForm):
    class Meta:
        model=article
        fields=[
            'article_author',
            'title',
            'body',
            'image',
            'catagory'


        ]

class registerUser(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'

         ]
