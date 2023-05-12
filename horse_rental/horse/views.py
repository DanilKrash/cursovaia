from django.shortcuts import render, get_object_or_404
from .models import Services


def main(request):
    return render(request, 'horse/main.html')


def service_detail_view(request, service_id):
    serv = get_object_or_404(Services, id=service_id)
    context = {'service': serv}
    return render(request, 'horse/service_detail.html', context)


def service_list_view(request):
    services = Services.objects.all()
    objects_count = Services.objects.count()
    context = {'service_list': services, 'objects_count': objects_count}
    return render(request, 'horse/service_list.html', context)

