from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def welcome(request):
    if 'next' in request.GET:
        if not request.user.is_authenticated():
            messages.error(request, "You're should login before continue.")
        else:
            messages.error(request, "Sorry, but you do not have permission for this action.")
    return render(request, 'accounts/welcome.html')


def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    to = 'welcome'
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.success(request, "You're successfully sign in!")
            to = request.POST.get('next') or to
        else:
            messages.warning(request, "Sorry, but your account disabled.")
    else:
        messages.warning(request, "Invalid login.")
    return redirect(to)


def sing_out(request):
    logout(request)
    messages.success(request, "You're successfully sign out!")
    return redirect('welcome')
