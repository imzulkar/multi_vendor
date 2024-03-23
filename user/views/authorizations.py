from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from user.models import User


def auth_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('shop:index_template'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.user_type == "SELLER":
                return HttpResponseRedirect(reverse_lazy('shop:products_list_template'))
            return HttpResponseRedirect(reverse_lazy('shop:index_template'))
        else:

            return render(request, 'user_auth.html', context={'message': 'Invalid credentials! Try again!'})
    else:
        return render(request, 'user_auth.html', context={})


@login_required
def logout_View(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('user:auth'))
