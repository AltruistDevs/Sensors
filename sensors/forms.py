from django import forms
from .models import Sensor

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'description', 'location', 'counter', 'token']
