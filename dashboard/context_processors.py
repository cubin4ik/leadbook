# following functions obtain data for "Summary" widget across "leadbook" app
# note: current date is generated inside templates with "now" command

from datetime import date, timedelta
from django.utils import timezone
from .scripts.api_handler import ParseAPI
from leads.models import Company
from business.models import Task, Project


class Widgets:
    """Widgets for specified user"""

    def __init__(self, user):
        self.user = user

    @staticmethod
    def get_today():
        return date.today().strftime('%d %b')

    @staticmethod
    def get_currency():
        return #round(get_currency())

    def get_leads(self):
        return Company.objects.filter(manager=self.user).count

    def get_new_leads(self):
        time_threshold = timezone.now() - timedelta(days=15)
        new_leads = Company.objects.filter(manager=self.user, date_created__gt=time_threshold).count
        return new_leads

    def get_tasks(self):
        return Task.objects.filter(executor=self.user).count

    def get_tasks_done(self):
        return Task.objects.filter(executor=self.user, done=True).count

    def get_projects(self):
        return Project.objects.filter(manager=self.user).count

    def get_hot_leads(self):
        return Company.get_hot_leads(self.user)


def summary(request):
    return {
        "global_week": date.today().isocalendar()[1],
        "global_currency": Widgets.get_currency(),

        # Below queryset functions are to serve specific users and are not global
        # "global_tasks": get_tasks(),
        # "global_tasks_done": get_tasks_done(),
        # "global_projects": get_projects(),
        # "global_leads": get_leads(),
        # "global_new_leads": get_new_leads()
    }


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

    return float(value.replace(",", "."))


