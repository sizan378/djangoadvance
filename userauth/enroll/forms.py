from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm


class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','last_name','username']