"""Forms of the project."""
from django import forms 
from .models import Thing


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields= ['name', 'description', 'quantity']
        widgets = {'description' : forms.Textarea()}
# Create your forms here.
