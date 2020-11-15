from django.db import models
from django.shortcuts import reverse


class Event(models.Model):
    # Type for the title
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

    title = models.CharField(max_length=5, choices=EventTitle.choices, default=EventTitle.EMAIL)
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


class Reminder(models.Model):  # TODO: rename to "Task"

    class ReminderImportance(models.TextChoices):
        URGENT = "4URG", "Urgent"
        HIGH = "3HI", "High"
        MEDIUM = "2MID", "Medium"
        LOW = "1LOW", "Low"
        FYI = "0FYI", "Info"

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
    manager = models.ForeignKey("accounts.User", related_name="reminder_manager", null=True, on_delete=models.SET_NULL)
    executor = models.ForeignKey("accounts.User", related_name="reminder_executor", null=True, on_delete=models.SET_NULL)

    class Meta:
        # sort by "the date" in descending order unless
        # overridden in the query with order_by()
        ordering = ["done", "-importance", "due_time"]

    def get_absolute_url(self):
        return reverse("business:reminder-detail", args=[self.id])

    def __str__(self):
        return self.task


class Project(models.Model):
    code = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, help_text="City of the project")
    short_description = models.CharField(max_length=100, help_text="Short description like facility's title")
    description = models.TextField(max_length=5000)
    volume = models.IntegerField(null=True, blank=True, help_text="Estimated project volume in euros")
    registry_date = models.DateTimeField()
    fulfilment_date = models.DateTimeField(null=True, blank=True)

    # foreign keys
    manager = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL)
    company = models.ManyToManyField("leads.Company", through="ProjectCompany")
    status = models.ForeignKey("ProjectStatus", on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey("ProjectStage", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["registry_date"]

    def get_absolute_url(self):
        return reverse("business:project-detail", args=[self.id])

    def __str__(self):
        return f"{self.code} {self.location} ({self.short_description})"


class ProjectCompany(models.Model):

    class RoleChoices(models.TextChoices):
        CONTRACTOR = "CTR", "Contractor"
        INTEGRATOR = "INT", "Integrator"
        END_USER = "EUS", "End User"
        PARTNER = "PRT", "Partner"

    role = models.CharField(max_length=3, choices=RoleChoices.choices, default=str(RoleChoices.CONTRACTOR))  # TODO: find out why it works only with str()
    project = models.ForeignKey("business.Project", on_delete=models.CASCADE)
    company = models.ForeignKey("leads.Company", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company}: {self.role} ({self.project})"


# TODO: change project status and stage to choice class
class ProjectStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class ProjectStage(models.Model):
    stage = models.CharField(max_length=100)

    def __str__(self):
        return self.stage


def project_file_path(instance, filename):
    return f"projects/{instance.project.pk}/documents/{filename}"


class ProjectDocument(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    document = models.FileField(upload_to=project_file_path)
    description = models.CharField(max_length=500)
