from django.contrib import admin
from .models import LegalForm, Company, Person, Email, Phone, Address


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = [PhoneInline, EmailInline]


admin.site.register(LegalForm)
admin.site.register(Company)
# admin.site.register(CompanyStatus)
admin.site.register(Person, PersonAdmin)
admin.site.register(Address)
