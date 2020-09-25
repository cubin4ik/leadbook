from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from datetime import datetime, timedelta
from .models import Project, Reminder, Event


class ProjectList(generic.ListView):
    paginate_by = 15
    model = Project
    extra_context = {
        "title": "Projects"
    }


class ProjectDetail(generic.DetailView):
    model = Project


class ProjectCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Project
    fields = "__all__"
    success_message = "New project has been successfully created"

    def get_initial(self):
        context = {"manager": self.request.user}

        for key, value in self.request.GET.items():
            context[key] = value
        return context


class ProjectUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Project
    fields = "__all__"
    success_message = "Project has been successfully updated"


class EventCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Event
    fields = "__all__"
    success_message = "New event has been successfully created"

    def get_initial(self):
        context = {"manager": self.request.user, "date": datetime.now()}

        for key, value in self.request.GET.items():
            context[key] = value
        return context


class EventDetail(generic.DetailView):
    model = Event


class EventUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Event
    fields = "__all__"
    success_message = "Event has been successfully updated"


class ReminderCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Reminder
    fields = ["task", "importance", "description", "due_time", "event", "company", "person", "project", "manager"]

    def get_initial(self):
        context = {"manager": self.request.user, "due_time": datetime.now() + timedelta(minutes=30)}
        print(context["manager"])

        for key, value in self.request.GET.items():
            context[key] = value

        return context


class ReminderUpdate(generic.UpdateView):
    model = Reminder
    fields = ["task", "importance", "description", "due_time", "event", "company", "person", "project"]
    success_message = "Reminder has been successfully updated"


class ReminderList(generic.ListView):
    model = Reminder


class ReminderDetail(generic.DetailView):
    model = Reminder
