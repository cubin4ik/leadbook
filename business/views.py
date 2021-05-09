from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from datetime import datetime, timedelta
from .models import Project, Task, Event, ProjectCompany, Document
from .forms import ProjectCreateForm, ProjectInlineFormSet


class ProjectList(LoginRequiredMixin, generic.ListView):
    paginate_by = 15
    model = Project
    extra_context = {
        "title": "Projects"
    }

    def get_queryset(self):
        search_fields = (
            "code__icontains",
            "location__icontains",
            "short_description__icontains",
            "description__icontains",
            "company__title__icontains",
        )

        self.extra_context.clear()  # Clearing context for paginator to properly work
        full_list = self.model.objects.filter(manager=self.request.user)

        if not self.request.GET.get('q', ''):
            object_list = full_list
        else:
            value = self.request.GET['q']
            print(f"ENTERED LOOP WITH q={value}")
            object_list = self.model.objects.none()

            for field in search_fields:
                new_set = full_list.filter(**{field: value})
                object_list = object_list.union(new_set)

        return object_list


class ProjectDetail(LoginRequiredMixin, generic.DetailView):
    # TODO: add attachments
    model = Project


class ProjectCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Project
    form_class = ProjectCreateForm
    success_message = "New project has been successfully created"
    extra_context = {
        "title": "Create New Project"
    }

    def get_initial(self):
        """Populate the form with data given in URL params"""
        ctx = {
            "manager": self.request.user,
            "registry_date": datetime.today()
        }

        for key, value in self.request.GET.items():
            ctx[key] = value
        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()
        inline_formset = ctx['inline_formset']

        if form.is_valid() and inline_formset.is_valid():
            self.object = form.save()
            print("ENTERED")

            new_companies = []
            for line in inline_formset:
                project_id = self.object
                company_id = line.cleaned_data.get('company')
                company_role = line.cleaned_data.get('role')

                if company_id and company_role:
                    new_companies.append(ProjectCompany(project=project_id, company=company_id, role=company_role))

            ProjectCompany.objects.filter(project=project_id).delete()
            ProjectCompany.objects.bulk_create(new_companies)

            # try:
            #     with transaction.atomic():
            #         # Replace the old with the new
            #         ProjectCompany.objects.filter(project=project_id).delete()
            #         ProjectCompany.objects.bulk_create(new_companies)
            #
            #         # And notify our users that it worked
            #         # messages.success(request, 'You have updated your profile.')
            #
            # except IntegrityError: #If the transaction failed
            #     messages.error(request, 'There was an error saving your profile.')
            #     return redirect(reverse('profile-settings'))

            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(ProjectCreate, self).get_context_data(**kwargs)

        if self.request.POST:
            ctx['inline_formset'] = ProjectInlineFormSet(self.request.POST)
        else:
            ctx['inline_formset'] = ProjectInlineFormSet()
        return ctx

    # Validation below has been recently replaced
    # def form_valid(self, form):
    #     self.object = form.save(commit=True)
    #
    #     # TODO: get an understanding of what is going on below
    #     # delete current mapping
    #     ProjectCompany.objects.filter(project=self.object).delete()  # TODO: how to avoid saving to database
    #
    #     # find or create (find if using soft delete)
    #     for company in form.cleaned_data['company']:
    #         project_company = ProjectCompany()
    #         project_company.project = self.object
    #         project_company.company = company
    #         # project_company.alive = True # if using soft delete
    #         project_company.save()
    #     return super(ModelFormMixin, self).form_valid(form)


class DocumentCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Document
    fields = "__all__"
    success_message = "New file has been successfully added"
    extra_context = {
        "title": "Add a document"
    }

    def get_initial(self):
        return self.request.GET


class ProjectUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Project
    form_class = ProjectCreateForm
    success_message = "Project has been successfully updated"

    def form_valid(self, form):
        ctx = self.get_context_data()
        inline_formset = ctx['inline_formset']

        with open("post_data_update_2.txt", "w") as wf:
            for key, value in self.request.POST.items():
                wf.write(key + "-" * 10 + str(value) + "\n")

        print("Entering")
        if form.is_valid() and inline_formset.is_valid():
            self.object = form.save()

            print("Entered")

            new_companies = []
            for line in inline_formset:
                project_id = self.object
                company_id = line.cleaned_data.get('company')
                company_role = line.cleaned_data.get('role')

                if company_id and company_role:
                    new_companies.append(ProjectCompany(project=project_id, company=company_id, role=company_role))

            ProjectCompany.objects.filter(project=project_id).delete()
            ProjectCompany.objects.bulk_create(new_companies)

            # try:
            #     with transaction.atomic():
            #         # Replace the old with the new
            #         ProjectCompany.objects.filter(project=project_id).delete()
            #         ProjectCompany.objects.bulk_create(new_companies)
            #
            #         # And notify our users that it worked
            #         # messages.success(request, 'You have updated your profile.')
            #
            # except IntegrityError: #If the transaction failed
            #     messages.error(request, 'There was an error saving your profile.')
            #     return redirect(reverse('profile-settings'))

            return redirect(self.get_success_url())
        else:
            print(f"Aborted: {form.is_valid()} {inline_formset.is_valid()}")
            for key, value in inline_formset:
                print(key, value)
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(ProjectUpdate, self).get_context_data(**kwargs)

        if self.request.POST:
            ctx['inline_formset'] = ProjectInlineFormSet(self.request.POST)
        else:
            ctx['inline_formset'] = ProjectInlineFormSet(instance=self.object)
        return ctx


class ProjectDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("business:projects")
    success_message = "The project has been successfully deleted."


class EventCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    # TODO: add attachments
    model = Event
    fields = "__all__"
    success_message = "New event has been successfully created"

    def get_initial(self):
        context = {"manager": self.request.user, "date": datetime.now()}

        for key, value in self.request.GET.items():
            context[key] = value
        return context


class EventDetail(LoginRequiredMixin, generic.DetailView):
    model = Event


class EventList(LoginRequiredMixin, generic.ListView):
    model = Event
    ordering = ['-date']


class EventUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Event
    fields = "__all__"
    success_message = "Event has been successfully updated"


class EventDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Event
    success_url = reverse_lazy("dashboard:home")
    success_message = "The event has been successfully deleted."


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Task
    fields = ["task", "importance", "description", "due_time", "event", "company", "person", "project", "manager", "executor"]
    success_message = "New task has been successfully created"

    def get_initial(self):
        context = {"manager": self.request.user, "executor": self.request.user, "due_time": datetime.now() + timedelta(minutes=30)}
        print(context["manager"])

        for key, value in self.request.GET.items():
            context[key] = value

        return context


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Task
    fields = ["task", "importance", "description", "due_time", "event", "company", "person", "project", "manager", "executor"]
    success_message = "Task has been successfully updated"


class TaskList(LoginRequiredMixin, generic.ListView):
    model = Task

    def get_queryset(self):
        object_list = self.model.objects.filter(executor=self.request.user) | self.model.objects.filter(manager=self.request.user)
        if "task" in self.request.GET.keys():
            task = self.request.GET["task"]
            object_list = object_list.filter(task__icontains=task) | object_list.filter(description__icontains=task)
            self.extra_context = {"query_request": task}

            # TODO: Revise code below
            if "my" in self.request.GET.keys():
                object_list = object_list.filter(executor=self.request.user)
        return object_list


class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("business:task-list")
    success_message = "The task has been successfully deleted."


@login_required
def task_set_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = bool(request.POST['done'])
    task.save()
    return HttpResponseRedirect(request.POST['next'])
