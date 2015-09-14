from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def welcome(request):
    if 'next' in request.GET:
        messages.error(request, "You're should login before continue.")
    return render(request, 'accounts/welcome.html')


def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.success(request, "You're successfully sign in!")
            return redirect(request.POST.get('next', 'welcome'))
        else:
            messages.warning(request, "Sorry, but your account disabled.")
    else:
        messages.warning(request, "Invalid login.")
    return redirect('welcome')


def sing_out(request):
    logout(request)
    messages.success(request, "You're successfully sign out!")
    return redirect('welcome')
