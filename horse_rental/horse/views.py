from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404, redirect
from .models import Services, Comments, Trainer, Horse, Feedback
from horse.forms import CommentForm, OrderForm, FeedbackForm
from django.core.paginator import Paginator, EmptyPage

from horse_reg.models import Profile


def main(request):
    cont = Feedback.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            form = FeedbackForm
    else:
        form = FeedbackForm()
    return render(request, 'horse/main.html', {'cont': cont, 'form': form})


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
    if request.method == 'POST':
        form = OrderForm(order_id, request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.services = order
            form.save()
            return redirect('/auth/my_orders/{{ user }}/')
    else:
        form = OrderForm(order_id)

    return render(request, 'horse/service_order.html', {'order': order, 'form': form})


def trainer_view(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    return JsonResponse({'sername': trainer.sername, 'date': trainer.date_of_employment, 'image': trainer.image.url, 'lastname': trainer.lastname})


def horse_view(request, horses_id):
    horses = get_object_or_404(Horse, id=horses_id)
    return JsonResponse({'breed': horses.breed, 'birthday': horses.birthday, 'horse_img': horses.horse_img.url, 'status': horses.status})
