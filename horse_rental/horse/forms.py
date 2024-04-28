from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput

from .models import Comments, Order, Services, Trainer, Horse, Feedback


class CommentForm(ModelForm):
    text = forms.CharField(label='Введите комментарий', widget=TextInput(attrs={"class": "comment_holder"}))

    class Meta:
        model = Comments
        fields = ('text',)


class OrderTrainerForm(forms.ModelForm):
    trainer = forms.ModelChoiceField(label='', queryset=Trainer.objects.all(),
                                     widget=forms.Select(attrs={"class": "form-select"}))
    horse = forms.ModelChoiceField(label='', queryset=Horse.objects.all(),
                                   widget=forms.Select(attrs={"class": "form-select"}))
    date_start = forms.DateTimeField(label='',
                                     widget=DateTimeInput(attrs={"class": "form-control", 'type': 'datetime-local'}))

    class Meta:
        model = Order
        fields = ('date_start', 'trainer', 'horse')

    def __init__(self, services_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        services = Services.objects.get(id=services_id)
        self.fields['trainer'].queryset = services.trainer.all()
        self.fields['horse'].queryset = services.horse.all()


class OrderForm(forms.ModelForm):
    horse = forms.ModelChoiceField(label='', queryset=Horse.objects.all(),
                                   widget=forms.Select(attrs={"class": "form-select"}))
    date_start = forms.DateTimeField(label='',
                                     widget=DateTimeInput(attrs={"class": "form-control", 'type': 'datetime-local'}))

    class Meta:
        model = Order
        fields = ('date_start', 'horse')

    def __init__(self, services_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        services = Services.objects.get(id=services_id)
        self.fields['horse'].queryset = services.horse.all()


class FeedbackForm(ModelForm):
    text = forms.CharField(label='',
                           widget=forms.Textarea(attrs={"class": "feedbacktext", "placeholder": 'Введите текст'}))

    class Meta:
        model = Feedback
        fields = ['text', ]
