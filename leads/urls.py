from django.urls import path
from . import views

app_name = 'leads'
urlpatterns = [
    path('', views.CompanyList.as_view(), name='companies'),
    path('new/', views.CompanyCreate.as_view(), name='companies-create'),
    path('<int:pk>/update/', views.CompanyUpdate.as_view(), name='companies-update'),
    path('<int:pk>/', views.CompanyDetail.as_view(), name='detail'),
    path('people/<int:pk>/', views.PersonDetail.as_view(), name='person-detail'),
    path('people/new/', views.PersonCreate.as_view(), name='person-create'),
    path('people/<int:pk>/update/', views.PersonUpdate.as_view(), name='person-update'),
    path('phone/new/', views.PhoneCreate.as_view(), name='phone-create'),
    path('email/new/', views.EmailCreate.as_view(), name='email-create'),
]
