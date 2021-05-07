from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Company, Person, Phone, Email
from .forms import PhoneCreateForm
from inventory.models import Discount


class CompanyList(generic.ListView, LoginRequiredMixin):
    paginate_by = 15
    model = Company
    extra_context = {
        'title': "Leads"
    }

    def get_queryset(self):

        search_attrs = {
            'q': (
                'title__icontains',
                'title_latin__icontains',
                'website__icontains',
                'about__icontains',
                'partners__title__icontains',
                'person__first_name__icontains',
                'person__last_name__icontains',
                'person__description__icontains',
            )
        }

        self.extra_context.clear()  # Clearing context for paginator to properly work

        if self.request.GET.get('hot', ''):
            self.extra_context['hot'] = 'true'
            return self.model.get_hot_leads(self.request.user)

        full_list = self.model.objects.filter(manager=self.request.user)

        if not self.request.GET:
            object_list = full_list
        else:
            query_params = {key: value for key, value in self.request.GET.items() if key in search_attrs.keys()}
            print("QUERY", query_params)
            # query_params = {}
            # for key, value in self.request.GET.items():
            #     print()
            #     query_params[key] = value

            object_list = self.model.objects.none()

            for key, value in query_params.items():

                if type(search_attrs[key]) is tuple:
                    for attr in search_attrs[key]:
                        new_set = full_list.filter(**{attr: value})
                        object_list = object_list.union(new_set)
                else:
                    new_set = full_list.filter(**{key: value})
                    object_list = object_list.union(new_set)

                self.extra_context[key] = value
                print("CONTEXT:---------------------", self.extra_context)

        return object_list


class CompanyDetail(generic.DetailView):
    model = Company
    # template_name = 'leads/company_detail.html'

    extra_context = {
        'title': "Detail"
    }


class CompanyCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Company
    fields = ["title", "legal_form", "title_latin", "website", "about", "status", "partners","discounts", "manager"]
    success_message = "New company has been successfully created"

    def get_initial(self):
        context = {"manager": self.request.user,
                   "discounts": Discount.objects.filter(product_group__title="FAFC", status="EU", turnover_class="D")}
        for key, value in self.request.GET.items():
            context[key] = value
        return context
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CompanyUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Company
    fields = ["title", "legal_form", "title_latin", "website", "about", "status", "partners", "discounts", "manager"]
    success_message = "Company has been successfully updated"


class PersonDetail(generic.DetailView):
    model = Person


class PersonCreate(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Person
    # fields = ["first_name", "last_name", "role", "company"]
    fields = "__all__"
    success_message = "New person has been successfully created"

    def get_initial(self):
        print(self.request.GET)
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
    form_class = PhoneCreateForm
    success_message = "New phone has been successfully created"
    extra_context = {
        'title': 'Create new phone number'
    }

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
