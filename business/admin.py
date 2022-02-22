from django.contrib import admin
from .models import Project, Task, Event, ProjectStatus, ProjectStage, ProjectCompany, Document

admin.site.register(Event)
admin.site.register(Project)
admin.site.register(ProjectStatus)
admin.site.register(ProjectStage)
admin.site.register(Task)
admin.site.register(ProjectCompany)
admin.site.register(Document)
