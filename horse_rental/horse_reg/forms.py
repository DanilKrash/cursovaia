from django import forms as dj_forms
from django.contrib.auth import forms
from horse_reg.models import CustomUser


class CustomUserRegister(forms.UserCreationForm):
    username = dj_forms.CharField(max_length=30, min_length=5, label='Логин')
    email = dj_forms.EmailField(max_length=128, label='Эл. почта')
    name = dj_forms.CharField(max_length=30, label='Имя')
    last_name = dj_forms.CharField(max_length=30, label='Фамилия')
    password1 = dj_forms.CharField(max_length=30, widget=dj_forms.PasswordInput, label='Пароль')
    password2 = dj_forms.CharField(max_length=30, widget=dj_forms.PasswordInput, label='Повторите пароль')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', 'last_name', 'password1', 'password2')

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, item in self.fields.item():
            item.widget.attrs['class'] = 'form-control'
            item.help_txt = ''
