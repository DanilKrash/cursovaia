from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from horse_reg.forms import CustomUserRegister, ProfileForm
from horse_reg.models import CustomUser, Profile
from django.conf import settings
from django.core.mail import send_mail
from horse.models import Order


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserRegister
    template_name = 'horse_reg/register.html'
    success_url = reverse_lazy('main:main')

    def post(self, request, *args, **kwargs):
        if self.form_class(request.POST).is_valid():
            message = render(request, 'horse_reg/verif_register.html')
            send_mail(subject='Регистрация на сайте',
                      message='Для подтверждения перейдите по ссылке http://127.0.0.1:8000/',
                      from_email=settings.EMAIL_HOST_USER, recipient_list=[request.POST.get('email')])
        result = super().post(request, *args, **kwargs)
        return result


def profile(request):
    prof = Profile.objects.filter(user=request.user)
    order = Order.objects.filter(user=request.user)
    return render(request, 'horse_reg/profile.html', {'prof': prof, 'order': order})


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('reg:profile')
    else:
        form = ProfileForm()
    return render(request, 'horse_reg/create_profile.html', {'form': form})


def update_profile(request):
    prof = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(instance=prof, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reg:profile')
    else:
        form = ProfileForm(instance=prof)
    return render(request, 'horse_reg/update_profile.html', {'form': form, 'prof': prof})
