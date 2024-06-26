from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
defuser_login(request):
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
    return render(request, 'account/Login.html, {'form': form})