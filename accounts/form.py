from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        # ('id', 'username', 'first_name', 'last_name', 'email', 'type', 'password')