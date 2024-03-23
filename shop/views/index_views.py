from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


def index_view(request):
    user = request.user
    if user.is_authenticated:
        if request.user.user_type == "SELLER":
            return HttpResponseRedirect(reverse_lazy('shop:products_list_template'))
    return HttpResponseRedirect(reverse_lazy('shop:shopping_template'))

    # return HttpResponseRedirect(reverse_lazy('user:auth'))
