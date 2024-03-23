from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from inventory.models import Products


@login_required(login_url='{% url "user:auth" %}')
def cart_views(request):
    user = request.user
    if user.is_authenticated:
        if request.user.user_type == "BUYER":
            return render(request, 'cart.html')

        return HttpResponseRedirect(reverse_lazy('shop:cart_template'))

    return HttpResponseRedirect(reverse_lazy('user:auth'))


@login_required(login_url='{% url "user:auth" %}')
def my_cart_views(request):
    user = request.user
    if user.is_authenticated:
        if request.user.user_type == "BUYER":
            return render(request, 'my_cart.html')

    return HttpResponseRedirect(reverse_lazy('shop:index_template'))
