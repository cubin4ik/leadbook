# following functions obtain data for "Summary" widget across "leadbook" app
# note: current date is generated inside templates with "now" command

from datetime import date, timedelta
from django.utils import timezone
from .scripts.apihandle import ParseAPI
from leads.models import Company
from business.models import Reminder, Project


def summary(request):
    return {
        "global_week": date.today().isocalendar()[1],
        "global_currency": 87,  # get_currency(),
        "global_tasks": get_tasks(),
        "global_tasks_done": get_tasks_done(),
        "global_projects": get_projects(),
        "global_leads": get_leads(),
        "global_new_leads": get_new_leads()
    }


def get_leads():
    return Company.objects.count


def get_new_leads():
    time_threshold = timezone.now() - timedelta(days=15)
    new_leads = Company.objects.filter(date_added__gt=time_threshold).count
    return new_leads


def get_currency():
    source_api = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002'
    par = 'date_req'
    value = date.today().strftime('%d/%m/%Y')

    pars = {
        'query': f'{par}={value}'
    }

    my_req = ParseAPI(source_api, **pars)

    for child in my_req.root:
        currency = child.find('CharCode').text
        if currency == "EUR":
            value = child.find('Value').text

    return value


def get_tasks():
    return Reminder.objects.count


def get_tasks_done():
    return Reminder.objects.filter(done=True).count


def get_projects():
    return Project.objects.count
