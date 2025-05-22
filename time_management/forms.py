from django import forms
from .models import Time


class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ["console_time", "computer_time", "mobile_time", "television_time"]
