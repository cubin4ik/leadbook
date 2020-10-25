from django.contrib import admin
from .models import Project, Reminder, Event, ProjectStatus, ProjectStage, ProjectCompany

admin.site.register(Event)
admin.site.register(Project)
admin.site.register(ProjectStatus)
admin.site.register(ProjectStage)
admin.site.register(Reminder)
admin.site.register(ProjectCompany)
