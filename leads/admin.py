from django.contrib import admin
from .models import LegalForm, Company, Person, Email, Phone, Address


admin.site.register(LegalForm)
admin.site.register(Company)
# admin.site.register(CompanyStatus)
admin.site.register(Person)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Address)
