from urllib import request
from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
                )
            if user.is_active:
                login(request, user)
                return HttpResponse('Login Successful')
            else:
                return HttpResponse('Account Disabled')
        else:
            return HttpResponse('Invalid login attempt')
    else:
        form = LoginForm()
    return render(request, 'account/Login.html', {'form': form})