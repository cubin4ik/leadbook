from django.urls import path
from .views import (ProjectList,
                    ProjectDetail,
                    DocumentCreate,
                    TaskList,
                    TaskDetail,
                    ProjectCreate,
                    EventCreate,
                    ProjectUpdate,
                    ProjectDelete,
                    EventDetail,
                    EventList,
                    EventUpdate,
                    EventDelete,
                    TaskCreate,
                    TaskUpdate,
                    TaskDelete,
                    task_set_done)

app_name = 'business'
urlpatterns = [
    path('projects/', ProjectList.as_view(), name='projects'),
    path('projects/new/', ProjectCreate.as_view(), name='project-create'),
    path('docs/new/', DocumentCreate.as_view(), name='document-create'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/', ProjectUpdate.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDelete.as_view(), name='project-delete'),
    path('events/', EventList.as_view(), name='events'),
    path('events/new/', EventCreate.as_view(), name='event-create'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/<int:pk>/update/', EventUpdate.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', EventDelete.as_view(), name='event-delete'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/new/', TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update', TaskUpdate.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete', TaskDelete.as_view(), name='task-delete'),
    path('tasks/<int:task_id>/done', task_set_done, name='task-done')
]
