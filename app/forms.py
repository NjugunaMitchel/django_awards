from django.forms import ModelForm
from .models import Project,Reviews


class RatesForm(ModelForm):
    class Meta:
        model = Reviews
        fields= ['userability_rating','content_rating','design_rating']

class NewprojectForm(ModelForm):
    class Meta:
        model = Project
        fields=['username','image','link','description','technologies']