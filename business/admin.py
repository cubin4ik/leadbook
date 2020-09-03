from django.contrib import admin
from .models import Project, Reminder, Event, ProjectStatus

admin.site.register(Event)
admin.site.register(Project)
admin.site.register(ProjectStatus)
admin.site.register(Reminder)
