from django.db import models
from django.utils import timezone
from inventory.models import Discount
from django.shortcuts import reverse


class PersonRole(models.TextChoices):
    UNKNOWN = 'UNW', 'Неизвестно'
    GENERAL_MANAGER = "CEO", "Генеральный директор"
    EXECUTIVE_DIRECTOR = "EXD", "Исполнительный директор"
    DEPUTY_DIRECTOR = "DPD", "Заместитель директора"
    SALES_DIRECTOR = "SAD", "Директор по продажам"
    HEAD_OF_DEPARTMENT = "HDP", "Руководитель отдела"
    ENGINEER = "ENG", "Инженер"
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

    def get_absolute_url(self):
        return reverse("leads:person-detail", args=[self.id])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Company(models.Model):
    title = models.CharField(max_length=150)
    title_latin = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    about = models.TextField(max_length=5000, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    # foreign keys
    legal_form = models.ForeignKey("LegalForm", null=True, on_delete=models.SET_NULL)

    # status = models.ForeignKey("CompanyStatus", on_delete=models.SET_NULL, null=True)
    status_choices = (
        ("Unknown", "Unknown"),
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Blocked", "Blocked"),
        ("Competitor", "Competitor")
    )
    status = models.CharField(max_length=45, choices=status_choices, default="Unknown")
    discounts = models.ManyToManyField("inventory.Discount", help_text="Hold down “Control”, or “Command” on a Mac, "
                                                                       "to select more than one.")  # TODO: add project discount
    manager = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = (("title", "legal_form", "about"),)

    def get_absolute_url(self):
        return reverse("leads:detail", args=[self.id])

    def __str__(self):
        return f"{self.title}"


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


class Email(models.Model):
    email = models.EmailField(max_length=255)
    type = models.CharField(max_length=50, null=True)

    # foreign keys
    person = models.ForeignKey("Person", on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("leads:person-detail", args=[self.person.id])

    def __str__(self):
        return f"{self.email} : {self.person.first_name} {self.person.last_name}: ({self.type})"


class PhoneType(models.TextChoices):
    MAIN = "MAIN", "main"
    MOBILE = "MOB", "mobile"
    WORK = "WRK", "work"
    PERSONAL = "PRS", "personal"


class Phone(models.Model):
    country_code = models.CharField(max_length=15)
    area_code = models.CharField(max_length=15)
    number = models.CharField(max_length=15)
    extension = models.CharField(max_length=15, null=True, blank=True)
    type = models.CharField(max_length=4, choices=PhoneType.choices, default=PhoneType.MAIN)

    # foreign keys
    # type = models.ForeignKey("PhoneType", on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = (("country_code", "area_code", "number", "extension"),)

    def get_absolute_url(self):
        return reverse("leads:person-detail", args=[self.person.id])

    def __str__(self):
        return f"+{self.country_code} ({self.area_code}) {self.number[:3]}-{self.number[3:5]}-{self.number[5:]} :" \
               f" {self.person.first_name} {self.person.last_name} ({self.type})"


# class PhoneType(models.Model):
#     type = models.CharField(max_length=45)
#
#     def __str__(self):
#         return self.type


class Address(models.Model):
    country = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    building = models.IntegerField()
    office = models.CharField(max_length=10, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)

    # foreign keys
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
