from django import forms
from django.forms import ModelForm
from .models import Student

class studentregistration(forms.Form):
    stuid = forms.IntegerField()
    name = forms.CharField()
    email = forms.EmailField()
    stupass = forms.CharField()

class studentform(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"