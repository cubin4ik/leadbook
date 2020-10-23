from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Company, Person, Phone, Email
from inventory.models import Discount


class CompanyList(generic.ListView):
    paginate_by = 15
    model = Company
    extra_context = {
        'title': "Leads"
    }

    def get_queryset(self):
        if "title" in self.request.GET.keys():
            title = self.request.GET.get("title")
            object_list = self.model.objects.filter(title__icontains=title) | self.model.objects.filter(about__icontains=title)
            if not object_list:
                object_list = self.model.objects.filter(person__first_name__icontains=title) | self.model.objects.filter(person__last_name__icontains=title)
            self.extra_context['query_request'] = title
        else:
            object_list = self.model.objects.all()
            self.extra_context['query_request'] = ""
        return object_list


class CompanyDetail(generic.DetailView):
    model = Company
    # template_name = 'leads/company_detail.html'

    extra_context = {
        'title': "Detail"
    }


class CompanyCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Company
    fields = ["title", "legal_form", "title_latin", "website", "about", "status", "discounts", "manager"]
    success_message = "New company has been successfully created"

    def get_initial(self):
        context = {"manager": self.request.user,
                   "discounts": Discount.objects.filter(product_group__title="FAFC", status="EU", turnover_class="D")}
        for key, value in self.request.GET.items():
            context[key] = value
        return context


class CompanyUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Company
    fields = ["title", "legal_form", "title_latin", "website", "about", "status", "discounts", "manager"]
    success_message = "Company has been successfully updated"


class PersonDetail(generic.DetailView):
    model = Person


class PersonCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Person
    # fields = ["first_name", "last_name", "role", "company"]
    fields = "__all__"
    success_message = "New person has been successfully created"

    def get_initial(self):
        return self.request.GET
        # Other options:

        # print("NOW SEE" + "-" * 30)
        # for k, v in self.request.META.items():
        #     print(k, v)

        # if "company" in self.request.GET.keys():
        #     company = self.request.GET.get("company")
        #     return {"company": company}

        # context = {}
        # for key, value in self.request.GET.items():
        #     context[key] = value
        # return context

        # if "HTTP_REFERER" in self.request.META:
        #     url_referer = self.request.META["HTTP_REFERER"]
        #     company = url_referer[-2]
        #     return {"company": company}


class PersonUpdate(generic.UpdateView):
    model = Person
    fields = "__all__"
    success_message = "Person has been successfully updated"


class PhoneCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Phone
    fields = "__all__"
    success_message = "New phone has been successfully created"

    def get_initial(self):
        context = {"country_code": 7}
        for key, value in self.request.GET.items():
            context[key] = value
        return context


class EmailCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Email
    fields = "__all__"
    success_message = "New email has been successfully created"

    def get_initial(self):
        return self.request.GET

# def leads(request):
#     companies_list = Company.objects.all()
#     context = {
#         'title': "Leads",
#         'today': timezone.now(),
#         'week': date.today().isocalendar()[1],
#         'companies_list': companies_list
#     }
#     return render(request, 'leads/leads.html', context)
