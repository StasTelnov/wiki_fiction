from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def welcome(request):
    return render(request, 'accounts/welcome.html')


def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        # else:
            # Return a 'disabled account' error message
    # else:
        # Return an 'invalid login' error message.
    return render(request, 'accounts/welcome.html')


def sing_out(request):
    logout(request)
    return render(request, 'accounts/welcome.html')