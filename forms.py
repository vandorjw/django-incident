from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from incident.models import Incident, Update


class IncidentUpdateForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['is_resolved', ]

UpdateFormSet = inlineformset_factory(
    Incident,
    Update,
    extra=1, )
