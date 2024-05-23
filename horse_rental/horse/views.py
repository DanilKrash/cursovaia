from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404, redirect

from .forms import OrderTrainerForm
from .models import Services, Comments, Trainer, Horse, Feedback
from horse.forms import CommentForm, OrderForm, FeedbackForm
from django.core.paginator import Paginator, EmptyPage

from horse_reg.models import Profile


def main(request):
    cont = Feedback.objects.filter(elect=True)
    user_ids = list(map(lambda item: item.user.id, cont))
    prof = Profile.objects.filter(user__id__in=user_ids)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            form = FeedbackForm
    else:
        form = FeedbackForm()
    return render(request, 'horse/main.html', {'cont': zip(cont, prof), 'form': form})


def service_list_view(request, page_num=1):
    search = request.GET.get('search', '')
    if search:
        services = Services.objects.filter(service_name__iregex=search)
    else:
        services = Services.objects.all()
    paginator = Paginator(services, 3)
    try:
        page_object = paginator.page(page_num)
    except EmptyPage:
        if page_num < 1:
            page_object = paginator.page(1)
        else:
            page_object = paginator.page(paginator.num_pages)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page': page_object, 'page_obj': page_obj}
    return render(request, 'horse/service_list.html', context)


def service_detail_view(request, service_id):
    serv = get_object_or_404(Services, id=service_id)
    comments = Comments.objects.filter(services=service_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.services = serv
            form.save()
            form = CommentForm
    else:
        form = CommentForm()
    return render(request, 'horse/service_detail.html', {'service': serv, 'comments': comments, 'form': form})


@login_required(login_url='reg:login')
def order_view(request, order_id):
    order = get_object_or_404(Services, id=order_id)
    form1 = OrderTrainerForm(order_id)
    form2 = OrderForm(order_id)
    if request.method == 'POST':
        form1 = OrderTrainerForm(order_id, request.POST)
        form2 = OrderForm(order_id, request.POST)
        if form1.is_valid() and 'trainer' in request.POST:
            form1.instance.services = order
            # if form1.instance.is_time_slot_available():
            if not form1.instance.trainer.is_busy:
                if not form1.instance.horse.is_busy:
                    form1.instance.save_trainer()
                    form1.instance.save_horse()
                    form = form1.save(commit=False)
                    form.user = request.user
                    form.services = order
                    form.save()
                    return redirect('reg:my_orders', request.user.username)
                else:
                    form1.add_error(None, "Данная лошадь уже занята")
            else:
                form1.add_error(None, "Данный тренер уже занят")
            # else:
            #     form1.add_error(None, "Данное время уже занято")
        elif form2.is_valid() and 'trainer' not in request.POST:
            form2.instance.services = order
            # if form2.instance.is_time_slot_available():
            if not form2.instance.horse.is_busy:
                form2.instance.save_horse()
                form = form2.save(commit=False)
                form.user = request.user
                form.services = order
                form.save()
                return redirect('reg:my_orders', request.user.username)
            else:
                form2.add_error(None, "Данная лошадь уже занята")
            # else:
            #     form2.add_error(None, "Данное время уже занято")

    return render(request, 'horse/service_order.html', {'order': order, 'form1': form1, 'form2': form2})


def trainer_view(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    return JsonResponse({'sername': trainer.sername, 'date': trainer.date_of_employment, 'image': trainer.image.url,
                         'lastname': trainer.lastname})


def horse_view(request, horses_id):
    horses = get_object_or_404(Horse, id=horses_id)
    return JsonResponse({'breed': horses.breed, 'birthday': horses.birthday, 'horse_img': horses.horse_img.url,
                         'status': horses.is_busy})
