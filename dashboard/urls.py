from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.Dashboard.as_view(), name='home'),
    path('site-search/', views.SiteSearch.as_view(), name='site-search'),
    path('settings/', views.settings, name='settings')
]