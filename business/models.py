from django.db import models
from django.shortcuts import reverse


class EventTitle(models.TextChoices):
    PHONE = "TEL", "Phone call"
    EMAIL = "EMAIL", "Email"
    MEETING = "MEET", "Meeting"
    SKYPE = "SKYPE", "Skype call"
    CONFERENCE = "CONF", "Conference"
    TRAIN = "TRAIN", "Training"
    ORDER = "ORDER", "Order"
    INCIDENT = "INCID", "Incident"
    FAIR = "FAIR", "Trade fair"
    FORUM = "FORUM", "Forum"


class Event(models.Model):
    title = models.CharField(max_length=5, choices=EventTitle.choices, default=EventTitle.MEETING)
    date = models.DateTimeField()
    description = models.TextField(max_length=5000)

    # foreign keys
    company = models.ManyToManyField("leads.Company")
    person = models.ManyToManyField("leads.Person")
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True, blank=True)
    manager = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering= ['date']

    def get_absolute_url(self):
        return reverse("business:event-detail", args=[self.id])

    def __str__(self):
        return f"{self.title} ({self.date}): {self.company.all()}"


class ReminderImportance(models.TextChoices):
    URGENT = "4URG", "Urgent"
    HIGH = "3HI", "High"
    MEDIUM = "2MID", "Medium"
    LOW = "1LOW", "Low"
    FYI = "0FYI", "Info"


class Reminder(models.Model):  # TODO: rename to "Task"
    task = models.CharField(max_length=45)
    description = models.TextField(max_length=5000)
    due_time = models.DateTimeField()
    done = models.BooleanField(default=False)
    importance = models.CharField(max_length=4, choices=ReminderImportance.choices, default=ReminderImportance.LOW)

    # test_choices = (
    #     ("TEST1", "Hello"),
    #     ("TEST2", "This"),
    #     ("TEST3", "Works"),
    #     ("TEST4", "Hello")
    # )
    # test_choices_field = models.CharField(max_length=20, null=True, choices=test_choices)

    # foreign keys
    event = models.ForeignKey("business.Event", on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey("leads.Company", on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey("leads.Person", on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True, blank=True)
    manager = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL)

    class Meta:
        # sort by "the date" in descending order unless
        # overridden in the query with order_by()
        ordering = ["-importance", "due_time"]

    def get_absolute_url(self):
        return reverse("business:reminder-detail", args=[self.id])

    def __str__(self):
        return self.task


class Project(models.Model):
    code = models.CharField(max_length=100)
    location = models.CharField(max_length=100, help_text="City of the project")
    short_description = models.CharField(max_length=100, help_text="Short description like facility's title")
    description = models.TextField(max_length=5000)
    volume = models.IntegerField(null=True, blank=True, help_text="Estimated project volume in euros")
    registry_date = models.DateTimeField()
    fulfilment_date = models.DateTimeField(null=True, blank=True)

    # foreign keys
    manager = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL)
    company_contractor = models.ForeignKey("leads.Company", related_name="project_contractor", on_delete=models.SET_NULL, null=True)
    company_integrator = models.ForeignKey("leads.Company", related_name="project_integrator", on_delete=models.SET_NULL, null=True, blank=True)
    company_end_user = models.ForeignKey("leads.Company", related_name="project_end_user", on_delete=models.SET_NULL, null=True, blank=True)
    # company = models.ManyToManyField("leads.Company", through="ProjectCompany")
    status = models.ForeignKey("ProjectStatus", on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey("ProjectStage", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["registry_date"]

    def get_absolute_url(self):
        return reverse("business:project-detail", args=[self.id])

    def __str__(self):
        return f"{self.code} {self.location} ({self.short_description})"


# class ProjectCompany(models.Model):
#     project = models.ForeignKey("business.Project", on_delete=models.SET_NULL, null=True)
#     company = models.ForeignKey("leads.Company", on_delete=models.SET_NULL, null=True)
#     role = models.CharField(max_length=500)


# TODO: change project status and stage to choice class
class ProjectStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class ProjectStage(models.Model):
    stage = models.CharField(max_length=100)

    def __str__(self):
        return self.stage