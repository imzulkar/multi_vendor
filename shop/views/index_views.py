from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy


@login_required(login_url='{% url "user:auth" %}')
def index_view(request):
    user = request.user
    if user.is_authenticated:
        if request.user.user_type == "SELLER":
            return HttpResponseRedirect(reverse_lazy('shop:products_list_template'))
        return HttpResponseRedirect(reverse_lazy('shop:cart_template'))

    return HttpResponseRedirect(reverse_lazy('user:auth'))
