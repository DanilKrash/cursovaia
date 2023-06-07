from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from horse_reg.forms import CustomUserRegister
from horse_reg.models import CustomUser
from django.conf import settings
from django.core.mail import send_mail


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserRegister
    template_name = 'horse_reg/register.html'
    success_url = reverse_lazy('hor:first_service')

    def post(self, request, *args, **kwargs):
        if self.form_class(request.POST).is_valid():
            message = render(request, 'horse_reg/verif_register.html')
            send_mail(subject='Регистрация на сайте', message='Для подтверждения перейдите по ссылке', from_email=settings.EMAIL_HOST_USER, recipient_list=[request.POST.get('email')])
        result = super().post(request, *args, **kwargs)
        return result



