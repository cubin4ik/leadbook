from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register, profile

app_name = 'accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name='logout')
]