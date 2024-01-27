# forms.py
from django import forms
from .models import FormSubmission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = ['full_name', 'email', 'phone_number', 'comments']
