from django import forms

from .models import Problems

class ProblemsForm(forms.ModelForm):
    class Meta:
        model = Problems
        exclude = ['status', 'story']

class ProblemsUpdateForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = ['status', 'story']
