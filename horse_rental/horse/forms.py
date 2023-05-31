from django import forms
from django.forms import ModelForm, TextInput
from .models import Comments


class CommentForm(ModelForm):
    text = forms.CharField(label='Введите комментарий', widget=TextInput(attrs={"class": "comment_holder"}))

    class Meta:
        model = Comments
        fields = ('text',)
