from django import forms
from contacts.models import Feedback
from django.forms import ModelForm, Textarea


class FeedbackForm(ModelForm):
    text = forms.CharField(label='', widget=Textarea(attrs={"class": "feedbacktext", "placeholder": 'Введите текст'}))

    class Meta:
        model = Feedback
        fields = ['text', ]
