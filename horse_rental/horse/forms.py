from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput
from .models import Comments, Order


class CommentForm(ModelForm):
    text = forms.CharField(label='Введите комментарий', widget=TextInput(attrs={"class": "comment_holder"}))

    class Meta:
        model = Comments
        fields = ('text',)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('date_start', 'trainer', 'horse')
        widgets = {
            'date_start': DateTimeInput(attrs={
                'class': 'comment_holder',
                'type': 'datetime-local',
            }),
        }


