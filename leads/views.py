from django.views import generic
from .models import Company, Person, Phone, Email


class CompanyList(generic.ListView):
    paginate_by = 20
    model = Company
    extra_context = {
        'title': "Leads"
    }


class CompanyDetail(generic.DetailView):
    model = Company
    # template_name = 'leads/company_detail.html'

    extra_context = {
        'title': "Detail"
    }


class CompanyCreate(generic.CreateView):
    model = Company
    fields = ["title", "title_latin", "about", "legal_form", "status", "discounts", "manager"]
    success_url = "/companies"


class CompanyUpdate(generic.UpdateView):
    model = Company
    fields = ["title", "about", "legal_form", "status", "discounts", "manager"]
    success_url = "/companies"


class PersonDetail(generic.DetailView):
    model = Person


class PersonCreate(generic.CreateView):
    model = Person
    # fields = ["first_name", "last_name", "role", "company"]
    fields = "__all__"
    success_url = "/"


class PhoneCreate(generic.CreateView):
    model = Phone
    fields = "__all__"
    success_url = "/"


class EmailCreate(generic.CreateView):
    model = Email
    fields = "__all__"
    success_url = "/"


# def leads(request):
#     companies_list = Company.objects.all()
#     context = {
#         'title': "Leads",
#         'today': timezone.now(),
#         'week': date.today().isocalendar()[1],
#         'companies_list': companies_list
#     }
#     return render(request, 'leads/leads.html', context)
