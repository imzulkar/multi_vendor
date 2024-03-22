from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render


def auth_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'user_auth.html', context={'user': user, 'message': 'Login successful.'})
        else:

            return render(request, 'user_atuh.html', context={'message': 'Login Failed.'})
    else:
        return render(request, 'user_auth.html', context={})
