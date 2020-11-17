from django.shortcuts import render
from django.views import generic
from leads.models import Company, Person


def dashboard(request):
    context = {
        'task': 'Dashboard',
        'low_activity_leads': get_low_activity_leads()
    }
    return render(request, 'dashboard/index.html', context)


def get_low_activity_leads():
    company_set = Company.objects.all()
    return company_set


class SiteSearch(generic.ListView):
    template_name = 'dashboard/site-search_list.html'

    def get_queryset(self):
        if 'site-search' in self.request.GET.keys():
            search_request = self.request.GET['site-search']
            object_list = Company.objects.filter(title__icontains=search_request) | Company.objects.filter(about__icontains=search_request)
        else:
            object_list = {}
        return object_list
