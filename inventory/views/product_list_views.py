from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='{% url "user:auth" %}')
def product_list(request):
    return render(request, 'products_list.html', context={})
