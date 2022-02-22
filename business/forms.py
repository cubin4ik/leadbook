from django.forms import ModelForm, inlineformset_factory, MultipleChoiceField
from .models import Project, ProjectCompany


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        exclude = ["company"]
        widgets = {
            "company": MultipleChoiceField
        }


class ProjectCompanyForm(ModelForm):
    class Meta:
        model = ProjectCompany
        fields = ("company", "role")


ProjectInlineFormSet = inlineformset_factory(
    Project,
    ProjectCompany,
    form=ProjectCompanyForm,
    extra=1,
    can_delete=True,
    can_order=False
)
