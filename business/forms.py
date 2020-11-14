from django.forms import ModelForm, inlineformset_factory, MultipleChoiceField
from .models import Project, ProjectCompany


class ProjectCreateForm(ModelForm):

    class Meta:
        model = Project
        exclude = ["company"]
        widgets = {
            "company": MultipleChoiceField
        }


class ProjectCompanyInline(ModelForm):
    class Meta:
        model = ProjectCompany
        fields = ("company", "role")


ProjectInlineFormSet = inlineformset_factory(
    Project,
    ProjectCompany,
    can_delete=True,
    form=ProjectCompanyInline,
    extra=3,
    max_num=4
)
