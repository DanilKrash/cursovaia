from django.shortcuts import render, get_object_or_404
from .models import Services, Comments, Trainer
from horse.forms import CommentForm, OrderForm
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage


def main(request):
    return render(request, 'horse/main.html')


def service_list_view(request, page_num=1):
    search = request.GET.get('search', '')
    if search:
        services = Services.objects.filter(service_name__icontains=search)
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


def order_view(request, order_id):
    order = get_object_or_404(Services, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.services = order
            form.user = request.user
            form.save()
            form = OrderForm
    else:
        form = OrderForm()

    return render(request, 'horse/service_order.html', {'order': order, 'form': form})
