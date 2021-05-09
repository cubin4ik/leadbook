from django.db import models


class Widget(models.Model):

    class WidgetSize(models.IntegerChoices):
        SINGLE = (1, "Single")
        DOUBLE = (2, "Double")
        QUADRUPLE = (4, "Quadruple")

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50, null=True, blank=True)
    url_path_name = models.CharField(max_length=100, default='dashboard:home')
    size = models.IntegerField(choices=WidgetSize.choices, default=WidgetSize.SINGLE)

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
