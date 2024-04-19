from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput

from .models import Comments, Order, Services, Trainer, Horse


class CommentForm(ModelForm):
    text = forms.CharField(label='Введите комментарий', widget=TextInput(attrs={"class": "comment_holder"}))

    class Meta:
        model = Comments
        fields = ('text',)


class OrderForm(forms.ModelForm):
    trainer = forms.ModelChoiceField(label='Введите комментарий', queryset=Trainer.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    horse = forms.ModelChoiceField(label='Введите комментарий', queryset=Horse.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))

    class Meta:
        model = Order
        fields = ('date_start', 'trainer', 'horse')
        widgets = {
            'date_start': DateTimeInput(attrs={
                'class': 'start_order',
                'type': 'datetime-local',
            }),
        }

    def __init__(self, services_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        services = Services.objects.get(id=services_id)
        self.fields['trainer'].queryset = services.trainer.all()
        self.fields['horse'].queryset = services.horse.all()
