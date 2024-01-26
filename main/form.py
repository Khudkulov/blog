from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'subject']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': "form-control",
            'name': "name",
            'id': "name",
            'placeholder': "Enter your name",
        })
        self.fields['email'].widget.attrs.update({
            'class': "form-control",
            'name': "email",
            'id': "email",
            'placeholder': "Enter email address",
        })
        self.fields['message'].widget.attrs.update({
            'class': "form-control w-100",
            'name': "message",
            'id': "message",
            'cols': 30,
            'rows': 9,
            'placeholder': "Enter Message",
        })
        self.fields['subject'].widget.attrs.update({
            'class': "form-control",
            'name': "subject",
            'id': "subject",
            'placeholder ': "Enter Subject",
        })


