from django.shortcuts import render
from leads.models import Company


def dashboard(request):
    context = {
        'title': 'Dashboard',
        'low_activity_leads': get_low_activity_leads()
    }
    return render(request, 'dashboard/index.html', context)


def get_low_activity_leads():
    company_set = Company.objects.all()
    return company_set
