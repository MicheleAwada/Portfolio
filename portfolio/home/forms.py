from django import forms
from contacters.models import contacts
class ContactForm(forms.ModelForm):

    class Meta:
        model = contacts
        fields = ["name", "email", "title", "body"]
        widgets = {
            'body': forms.Textarea(attrs={'cols': 40, 'rows': 10})  # Adjust the cols and rows as needed
        }