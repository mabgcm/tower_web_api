from django import forms
from tower_api.models import Period, Clss

class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ['course', 'period']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Clss
        fields = ['course', 'period', 'clss']
        labels = {'course': 'Course', 'period': 'Period', 'clss': 'Class'}
