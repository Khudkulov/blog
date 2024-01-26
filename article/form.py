from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message', 'website', 'image']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': "form-control",
            'placeholder': 'Name',
            'id': 'name'

        })
        self.fields['email'].widget.attrs.update({
            'class': "form-control",
            'placeholder': 'Email',
            'id': 'email'
        })
        self.fields['message'].widget.attrs.update({
            'class': "form-control w-100",
            'name': "comment",
            'id': "comment",
            'cols': 30,
            'rows': 9,
            'placeholder': "Write Comment",
        })
        self.fields['website'].widget.attrs.update({
            'class': "form-control",
            'placeholder': 'Website',
            'id': 'website'
        })
        self.fields['image'].widget.attrs.update({

        })
