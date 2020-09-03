from django.views import generic
from .models import Project, Reminder, Event


class ProjectList(generic.ListView):
    paginate_by = 20
    model = Project
    # extra_context = {
    #     'title': "Leads",
    #     'today': timezone.now(),
    #     'week': date.today().isocalendar()[1],
    # }


class ProjectDetail(generic.DetailView):
    model = Project


class ProjectCreate(generic.CreateView):
    model = Project
    fields = "__all__"
    success_url = "projects"


class EventCreate(generic.CreateView):
    model = Event
    fields = "__all__"
    success_url = "/"


class ReminderList(generic.ListView):
    model = Reminder


class ReminderDetail(generic.DetailView):
    model = Reminder
