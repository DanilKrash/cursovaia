from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from horse_reg.forms import CustomUserRegister, ProfileForm
from horse_reg.models import CustomUser, Profile, User
from django.conf import settings
from django.core.mail import send_mail
from horse.models import Order


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserRegister
    template_name = 'horse_reg/register.html'
    success_url = reverse_lazy('/auth/update_profile/{{ user.username }}/')

    def post(self, request, *args, **kwargs):
        if self.form_class(request.POST).is_valid():
            message = render(request, 'horse_reg/verif_register.html')
            send_mail(subject='Регистрация на сайте',
                      message='Для подтверждения перейдите по ссылке http://127.0.0.1:8000/',
                      from_email=settings.EMAIL_HOST_USER, recipient_list=[request.POST.get('email')])
        result = super().post(request, *args, **kwargs)
        return result


@login_required(login_url='reg:login')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    prof = get_object_or_404(Profile, user=user)
    order = Order.objects.filter(user=user)
    return render(request, 'horse_reg/profile.html', {'prof': prof, 'order': order, 'user': user})


@login_required(login_url='reg:login')
def create_profile(request, username):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/auth/profile/{{ user.username }}/')
    else:
        form = ProfileForm()
    return render(request, 'horse_reg/create_profile.html', {'form': form})


@login_required(login_url='reg:login')
def update_profile(request, username):
    prof = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(instance=prof, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/auth/profile/{{ user.username }}/')
    else:
        form = ProfileForm(instance=prof)
    return render(request, 'horse_reg/update_profile.html', {'form': form, 'prof': prof})


def my_orders(request, username):
    user = get_object_or_404(User, username=username)
    order = Order.objects.filter(user=user)
    total_sell = sum(order.services.service_sell for order in order)
    total_sale = sum(order.services.sale for order in order)
    total = (total_sell * (100 - total_sale) / 100)
    return render(request, 'horse_reg/my_orders.html', {'user': user, 'order': order, 'total': total})
