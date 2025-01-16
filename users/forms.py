from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    phone_number = forms.CharField(max_length=15, required=False)
   # profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    class Meta:
        fields = ['username', 'password']








# from django import forms
# from .models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm


# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')
#     phone_number = forms.CharField(max_length=15, required=False)
#     profile_picture = forms.ImageField(required=False)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'phone_number', 'profile_picture', 'password1', 'password2')

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255, widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username', 'password')