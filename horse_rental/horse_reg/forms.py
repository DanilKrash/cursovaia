from django import forms as dj_forms
from django.contrib.auth import forms
from django.forms import TextInput
from horse_reg.models import CustomUser, Profile


class CustomUserRegister(forms.UserCreationForm):
    username = dj_forms.CharField(max_length=30, min_length=5, label='Логин',
                                  widget=TextInput(attrs={"class": "auth_holder"}))
    email = dj_forms.EmailField(max_length=128, label='Эл. почта',
                                widget=TextInput(attrs={"class": "auth_holder"}))
    first_name = dj_forms.CharField(max_length=30, label='Имя',
                                    widget=TextInput(attrs={"class": "auth_holder"}))
    last_name = dj_forms.CharField(max_length=30, label='Фамилия',
                                   widget=TextInput(attrs={"class": "auth_holder"}))
    password1 = dj_forms.CharField(max_length=30, widget=dj_forms.PasswordInput(attrs={"class": "auth_holder"}),
                                   label='Пароль')
    password2 = dj_forms.CharField(max_length=30, widget=dj_forms.PasswordInput(attrs={"class": "auth_holder"}),
                                   label='Повторите пароль')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, item in self.fields.item():
            item.widget.attrs['class'] = 'auth_holder'


from django import forms


class ProfileForm(forms.ModelForm):
    phone = dj_forms.CharField(max_length=30, min_length=5, label='Номер телефона',
                               widget=TextInput(attrs={"class": "auth_holder"}))
    body = dj_forms.CharField(max_length=30, min_length=5, label='О себе',
                              widget=TextInput(attrs={"class": "auth_holder"}))
    img = forms.ImageField(label='', widget=forms.FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Profile
        fields = ('phone', 'img', 'body')
