from django.urls import path
from . import views
from leads.views import CompanyList

app_name = 'dashboard'
urlpatterns = [
    path('', views.Dashboard.as_view(), name='home'),
    path('site-search/', CompanyList.as_view(), name='site-search'),
    path('settings/', views.settings, name='settings')
]