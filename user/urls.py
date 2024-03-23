from django.urls import path
from user.views import auth_view, logout_View

app_name = 'user'
urlpatterns = [
    path('', auth_view, name='auth'),
    path('logout', logout_View, name='logout'),
]
