from django.db import models
from django.utils import timezone
from inventory.models import Discount
from django.shortcuts import reverse
from accounts.models import User
from datetime import timedelta
from time import time


class PersonRole(models.TextChoices):
    UNKNOWN = 'UNW', 'Неизвестно'
    GENERAL_MANAGER = "CEO", "Генеральный директор"
    EXECUTIVE_DIRECTOR = "EXD", "Исполнительный директор"
    CHIEF_TECHNICAL_OFFICER = "CTO", "Технический директор"
    DEPUTY_DIRECTOR = "DPD", "Заместитель директора"
    DIRECTOR = "DIR", "Директор"
    SALES_DIRECTOR = "SAD", "Директор по продажам"
    HEAD_OF_DEPARTMENT = " ", "Руководитель отдела"
    CHIEF_TECHNICAL_ENGINEER = "CTE", "Главный инженер"
    ENGINEER = "ENG", "Инженер"
    CONSTRUCTOR = "CNS", "Конструктор"
    DESIGNER = "DES", "Проектировщик"
    EXPERT = "EXP", "Эксперт"
    PURCHASING_SPECIALIST = "PUR", "Специалист закупки"
    PROGRAMMER = "PRG", "Программист"
    SALESMAN = "SAL", "Продавец"
    KEY_ACCOUNT_MANAGER = "KAM", "Ключевой менеджер по работе с Bosch"
    PARTNER_MANAGER = "MAN", "Менеджер по работе с партнерами"


class Person(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    # role_choices = (
    #     ("Директор", "Директор"),
    #     ("Генеральный директор", "Генеральный директор"),
    #     ("Исполнительный директор", "Исполнительный директор"),
    #     ("Руководитель отдела", "Руководитель отдела"),
    #     ("Инженер", "Инженер"),
    #     ("Специалист закупки", "Специалист закупки"),
    #     ("Программист", "Программист"),
    #     ("Продавец", "Продавец"),
    #     ("Ключевой менеджер по работе с Bosch", "Ключевой менеджер по работе с Bosch"),
    # )

    role = models.CharField(max_length=3, null=True, choices=PersonRole.choices, default=PersonRole.UNKNOWN)
    description = models.TextField(max_length=500, null=True, blank=True, help_text="Особенности работы с контрагентом")

    # foreign keys
    company = models.ForeignKey("Company", null=True, on_delete=models.SET_NULL)
    is_main_contact = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        # Making sure there is only one main person for a company
        if self.is_main_contact:
            try:
                old_main_contact = Person.objects.get(company=self.company, is_main_contact=True)
                if self != old_main_contact:
                    old_main_contact.is_main_contact = False
                    old_main_contact.save()
            except Person.DoesNotExist:
                pass

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("leads:person-detail", args=[self.id])

    def get_email(self):
        emails = Email.objects.filter(person=self)
        for email in emails:
            if email.type == "MAIN":
                return email
        return emails.first()

    def get_phone(self):
        phones = Phone.objects.filter(person=self)
        for phone in phones:
            if phone.type == "MAIN":
                return phone
        return phones.first()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Company(models.Model):
    title = models.CharField(max_length=150)
    title_latin = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    about = models.TextField(max_length=5000, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey("accounts.User", on_delete=models.SET_DEFAULT, default=User.objects.get(pk=3).pk, related_name="company_creator")

    # foreign keys
    legal_form = models.ForeignKey("LegalForm", null=True, on_delete=models.SET_NULL)

    # status = models.ForeignKey("CompanyStatus", on_delete=models.SET_NULL, null=True)
    status_choices = (
        ("ACT_LOY", "Active customer (loyal)"),
        ("ACT_DIS", "Active customer (disloyal)"),
        ("POT_LOY", "Potential customer (loyal)"),
        ("POT_CON", "Potential customer (in contact)"),
        ("POT_UNK", "Potential customer (not in contact)"),
        ("CMP_USF", "Competitor (useless)"),
        ("CMP_USL", "Competitor (useful)"),
        ("UNKNOWN", "Unknown"),
        ("BLOCKED", "Blocked")
    )
    status = models.CharField(max_length=7, choices=status_choices, default="UNKNOWN")
    discounts = models.ManyToManyField("inventory.Discount", help_text="Hold down “Control”, or “Command” on a Mac, "
                                                                       "to select more than one.")  # TODO: add project discount
    partners = models.ManyToManyField('self', blank=True)
    manager = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL, related_name="company_manager")

    class Meta:
        unique_together = (("title", "legal_form"),)

    def get_absolute_url(self):
        return reverse("leads:detail", args=[self.id])

    def __str__(self):
        return f"{self.title}"

    def get_main_contact(self):
        try:
            return self.person_set.get(is_main_contact=True)
        except Person.DoesNotExist:
            return None

    def get_phone(self):
        if self.get_main_contact():
            if self.get_main_contact().get_phone():
                return self.get_main_contact().get_phone()
        else:
            emps = self.person_set.all()  # Get all employees
            for emp in emps:
                if emp.get_phone():
                    phone = emp.get_phone()
                    return phone

    def get_email(self):
        if self.get_main_contact():
            if self.get_main_contact().get_email():
                return self.get_main_contact().get_email()
        else:
            emps = self.person_set.all()  # Get all employees
            for emp in emps:
                if emp.get_email():
                    email = emp.get_email()
                    return email

    def get_short_status(self):
        status = self.get_status_display().split(" ")[0]
        if status == "Active":
            color = "success"
        elif status == "Potential":
            color = "warning"
        else:
            color = "danger"
        return {"status": status, "color": color}

    @staticmethod
    def get_hot_leads(user):
        # return companies that need to be contacted

        # In a tuple: first value for new leads, second value for old leads in days
        events_frequency = {
            "ACT_LOY": (5, 45),
            "ACT_DIS": (5, 30),
            "POT_LOY": (5, 20),
            "POT_CON": (10, 45),
            "POT_UNK": (5, 45),
            "CMP_USF": (5, 45)
        }

        user_leads = Company.objects.filter(manager=user)

        hot_ids = []
        for lead in user_leads:
            if lead.status in events_frequency.keys():
                last_event_delta = timezone.now() - (lead.event_set.last().date if lead.event_set.count() else lead.date_created)
                if (timezone.now() - lead.date_created) > timedelta(days=90):
                    normal_frequency = events_frequency[lead.status][1]
                else:
                    normal_frequency = events_frequency[lead.status][0]

                if last_event_delta > timedelta(days=normal_frequency):
                    hot_ids.append(lead.id)

        print(user_leads.filter(id__in=hot_ids))
        return user_leads.filter(id__in=hot_ids)


# class CompanyStatus(models.Model):
#     status_choices = (
#         ("Unknown", "Unknown"),
#         ("Active", "Active"),
#         ("Inactive", "Inactive"),
#         ("Blocked", "Blocked"),
#         ("Competitor", "Competitor")
#     )
#     status = models.CharField(max_length=45, choices=status_choices, default=status_choices[0])
#
#     def __str__(self):
#         return self.status


class LegalForm(models.Model):
    short_form = models.CharField(max_length=15)
    long_form = models.CharField(max_length=50)

    def __str__(self):
        return self.short_form


class ContactType(models.TextChoices):
    MAIN = "MAIN", "main"
    MOBILE = "MOB", "mobile"
    WORK = "WRK", "work"
    PERSONAL = "PRS", "personal"
    PAST = "PST", "past"


class Email(models.Model):
    email = models.EmailField(max_length=255)
    type = models.CharField(max_length=4, choices=ContactType.choices, default=ContactType.MAIN)

    # foreign keys
    person = models.ForeignKey("Person", on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("leads:person-detail", args=[self.person.id])

    def __str__(self):
        return self.email


class Phone(models.Model):
    country_code = models.PositiveIntegerField()
    area_code = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    extension = models.PositiveIntegerField(null=True, blank=True)
    type = models.CharField(max_length=4, choices=ContactType.choices, default=ContactType.MAIN)

    # foreign keys
    # type = models.ForeignKey("ContactType", on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = (("country_code", "area_code", "number", "extension"),)

    def get_absolute_url(self):
        return reverse("leads:person-detail", args=[self.person.id])

    def __str__(self):
        phone = f"{self.country_code}{self.area_code}{self.number}"
        if self.extension:
            phone += f",{self.extension}"
        return phone
        # number_text = str(self.number)
        # return f"+{self.country_code} ({self.area_code}) {number_text[:3]}-{number_text[3:5]}-{number_text[5:]} :" \
        #        f" {self.person.first_name} {self.person.last_name} ({self.type})"


class Address(models.Model):
    country = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    building = models.IntegerField()
    office = models.CharField(max_length=10, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)

    # foreign keys
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
