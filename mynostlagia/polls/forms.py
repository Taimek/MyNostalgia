from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']

class CustomHTMLForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['custom_html']  # <-- to pole, które właśnie dodaliśmy w models.py
        widgets = {
            'custom_html': forms.Textarea(attrs={'rows': 20, 'cols': 100, 'placeholder': 'Wklej swój kod HTML + CSS tutaj...'}),
        }
