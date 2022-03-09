from django.shortcuts import render, HttpResponse, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import Signupform
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout

#Signup 
def sign_up(request):
    forms = Signupform()
    if request.method == 'POST':
        forms = Signupform(request.POST)
        if forms.is_valid():
            forms.save()
        else:
            forms = Signupform()
    return render(request, 'enroll/signup.html',{'form':forms})

#Login 
def login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=name,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        fm = AuthenticationForm()
    return render(request,'enroll/userlogin.html',{'form':fm})

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


#Password chagne
def user_change_password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm  = PasswordChangeForm(user= request.user)
    return render(request, 'enroll/changepass.html',{'form':fm})


