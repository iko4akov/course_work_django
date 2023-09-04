from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from user.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserProfile(UserChangeForm):

    class Meta:
        model = User
        fields = ['email', 'country', 'phone', 'avatar', 'check_email']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
        self.fields['check_email'].widget = forms.HiddenInput()
