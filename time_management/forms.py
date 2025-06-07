from django import forms
from .models import Time

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ["console_time", "computer_time", "mobile_time", "television_time"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial["console_time"] = 0
        self.initial["computer_time"] = 0
        self.initial["mobile_time"] = 0
        self.initial["television_time"] = 0
