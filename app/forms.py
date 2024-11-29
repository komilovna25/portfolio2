from django.forms import ModelForm
from .models import Contact
from django import forms
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", 'first_name',  "email"]

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        full_name = self.cleaned_data.get('full_name')
        if len(first_name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters.")
        return first_name

    # def clean_content(self):
    #     content = self.cleaned_data.get('content')
    #     if not content:
    #         raise forms.ValidationError("Subject must be entered.")
    #     return content