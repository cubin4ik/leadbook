from django.urls import path
from .views import ProjectList, ProjectDetail, ReminderList, ReminderDetail, ProjectCreate, EventCreate

app_name = 'business'
urlpatterns = [
    path('projects/', ProjectList.as_view(), name='projects'),
    path('projects/new/', ProjectCreate.as_view(), name='project-create'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('events/new/', EventCreate.as_view(), name='event-create'),
    path('reminders/', ReminderList.as_view(), name='reminder-list'),
    path('reminders/<int:pk>/', ReminderDetail.as_view(), name='reminder-detail')
]
