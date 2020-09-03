from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=45)
    date = models.DateTimeField()
    description = models.TextField(max_length=5000)

    # foreign keys
    company = models.ManyToManyField("leads.Company")
    person = models.ManyToManyField("leads.Person")
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True, blank=True)
    manager = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering= ['date']

    def __str__(self):
        return self.title


class Reminder(models.Model):  # TODO: rename to "Task"
    task = models.CharField(max_length=45)
    description = models.TextField(max_length=5000)
    due_time = models.DateTimeField()
    done = models.BooleanField(default=False)

    # foreign keys
    company = models.ForeignKey("leads.Company", on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey("leads.Person", on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True, blank=True)
    manager = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL)

    class Meta:
        # sort by "the date" in descending order unless
        # overridden in the query with order_by()
        ordering = ['due_time']

    def __str__(self):
        return self.task


class Project(models.Model):
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    volume = models.IntegerField(null=True, blank=True, help_text="Estimated project volume in euros")
    location = models.CharField(max_length=100)
    registry_date = models.DateTimeField()
    fulfilment_date = models.DateTimeField(null=True, blank=True)

    # foreign keys
    manager = models.ForeignKey("accounts.User", null=True, on_delete=models.SET_NULL)
    company_supplier = models.ForeignKey("leads.Company", related_name="project_supplier", on_delete=models.SET_NULL, null=True)
    company_integrator = models.ForeignKey("leads.Company", related_name="project_integrator", on_delete=models.SET_NULL, null=True, blank=True)
    company_end_user = models.ForeignKey("leads.Company", related_name="project_end_user", on_delete=models.SET_NULL, null=True, blank=True)
    # company = models.ManyToManyField("leads.Company", through="ProjectCompany")
    status = models.ForeignKey("ProjectStatus", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.code


# class ProjectCompany(models.Model):
#     project = models.ForeignKey("business.Project", on_delete=models.SET_NULL, null=True)
#     company = models.ForeignKey("leads.Company", on_delete=models.SET_NULL, null=True)
#     role = models.CharField(max_length=500)


class ProjectStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status
