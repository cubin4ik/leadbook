from django.urls import path
from .views import (ProjectList,
                    ProjectDetail,
                    ReminderList,
                    ReminderDetail,
                    ProjectCreate,
                    EventCreate,
                    ProjectUpdate,
                    ProjectDelete,
                    EventDetail,
                    EventUpdate,
                    EventDelete,
                    ReminderCreate,
                    ReminderUpdate,
                    ReminderDelete)

app_name = 'business'
urlpatterns = [
    path('projects/', ProjectList.as_view(), name='projects'),
    path('projects/new/', ProjectCreate.as_view(), name='project-create'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/', ProjectUpdate.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDelete.as_view(), name='project-delete'),
    path('events/new/', EventCreate.as_view(), name='event-create'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/<int:pk>/update/', EventUpdate.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', EventDelete.as_view(), name='event-delete'),
    path('reminders/', ReminderList.as_view(), name='reminder-list'),
    path('reminders/new/', ReminderCreate.as_view(), name='reminder-create'),
    path('reminders/<int:pk>/', ReminderDetail.as_view(), name='reminder-detail'),
    path('reminders/<int:pk>/update', ReminderUpdate.as_view(), name='reminder-update'),
    path('reminders/<int:pk>/delete', ReminderDelete.as_view(), name='reminder-delete')
]
