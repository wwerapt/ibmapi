from django import forms

class PersonaForm(forms.Form):
    GENDER_CHOICES = [(0, 'Female'), (1, 'Male')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender')
    age = forms.IntegerField(label='Age')

class LivingAreaForm(forms.Form):
    heatmap = forms.FloatField(initial=1)
    understand_customer = forms.FloatField(initial=1)
    income_per_head = forms.FloatField(initial=1)
    climate = forms.FloatField(initial=1)

class EventForm(forms.Form):
    marketing_media = forms.FloatField(initial=1)
    marketing_campaign = forms.FloatField(initial=1)
    marketing_touchpoint = forms.FloatField(initial=1)

class EventFormMedia(forms.Form):
    marketing_media = forms.FloatField(initial=1)
class EventFormCampaign(forms.Form):
    marketing_campaign = forms.FloatField(initial=1)
class EventFormTouchpoint(forms.Form):
    marketing_touchpoint = forms.FloatField(initial=1)

class DemandDateForm(forms.Form):
    date = forms.IntegerField(label='Day')

