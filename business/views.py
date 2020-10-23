from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
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


class ProjectDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("business:projects")
    success_message = "The project has been successfully deleted."


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


class EventDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Event
    success_url = reverse_lazy("dashboard:home")
    success_message = "The event has been successfully deleted."


class ReminderCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Reminder
    fields = ["task", "importance", "description", "due_time", "event", "company", "person", "project", "executor"]

    def get_initial(self):
        context = {"manager": self.request.user, "executor": self.request.user, "due_time": datetime.now() + timedelta(minutes=30)}
        print(context["manager"])

        for key, value in self.request.GET.items():
            context[key] = value

        return context


class ReminderUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Reminder
    fields = ["task", "importance", "description", "due_time", "event", "company", "person", "project", "executor"]
    success_message = "Reminder has been successfully updated"


class ReminderList(generic.ListView):
    model = Reminder

    def get_queryset(self):
        object_list = self.model.objects.filter(executor=self.request.user) | self.model.objects.filter(manager=self.request.user)
        if "task" in self.request.GET.keys():
            task = self.request.GET["task"]
            object_list = object_list.filter(task__icontains=task) | object_list.filter(description__icontains=task)
            self.extra_context = {"query_request": task}

            # TODO: Revise code below
            if "mine" in self.request.GET.keys():
                object_list = object_list.filter(executor=self.request.user)
        return object_list


class ReminderDetail(generic.DetailView):
    model = Reminder


class ReminderDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Reminder
    success_url = reverse_lazy("business:reminder-list")
    success_message = "The reminder has been successfully deleted."


def reminder_set_done(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    reminder.done = bool(request.POST['done'])
    reminder.save()
    return HttpResponseRedirect(request.POST['next'])
