from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from leads.models import Company, Person
from .models import Widget
from .context_processors import Widgets

# Below imports are for demonstration of a lower level programming
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


# The following code is replaced by a class based view
# def dashboard(request):
#
#     context = {
#         'title': 'Dashboard',
#         'low_activity_leads': Company.objects.all(),
#         'widgets': [],
#     }
#
#     widgets = Widget.objects.filter(account=request.user)
#     for widget in widgets:
#         widget_command = "get_" + widget.title
#         if widget_command in dir(Widgets):
#             widget.value = getattr(Widgets, widget_command)()
#         context["widgets"].append(widget)
#
#     return render(request, 'dashboard/index.html', context)


class Dashboard(generic.ListView, LoginRequiredMixin):
    model = Widget
    template_name = "dashboard/index.html"
    extra_context = {
        'title': 'Dashboard'
    }

    def get_queryset(self):
        widgets = self.request.user.widgets.all()
        self.user_widgets = Widgets(self.request.user)

        for widget in widgets:
            widget_command = "get_" + widget.title.replace(" ", "_")
            if widget_command in dir(Widgets):
                widget.value = getattr(self.user_widgets, widget_command)()
                widget.type = type(widget.value).__name__
        return widgets

        # def get_context_data(self, **kwargs):
        #     ctx = super(Dashboard, self).get_context_data(**kwargs)
        #
        #     ctx['hot_leads'] = self.user_widgets.get_hot_leads()
        #     return ctx


@login_required
def settings(request):
    if request.method == "POST":
        widgets = request.POST
        for widget in widgets:
            print(len(widget))
            print(widget)
        user = request.user
    template = loader.get_template('dashboard/settings.html')
    context = {
        'widgets': Widget.objects.all()
    }
    return HttpResponse(template.render(context, request))


class SiteSearch(generic.ListView):
    template_name = 'dashboard/site-search_list.html'

    def get_queryset(self):
        if 'site-search' in self.request.GET.keys():
            search_request = self.request.GET['site-search']
            object_list = Company.objects.filter(title__icontains=search_request) | Company.objects.filter(about__icontains=search_request)
        else:
            object_list = {}
        return object_list
