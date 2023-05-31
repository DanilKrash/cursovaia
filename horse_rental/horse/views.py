from django.shortcuts import render, get_object_or_404
from .models import Services, Comments
from horse.forms import CommentForm


def main(request):
    return render(request, 'horse/main.html')


def service_list_view(request):
    services = Services.objects.all()
    objects_count = Services.objects.count()
    context = {'service_list': services, 'objects_count': objects_count}
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
        context = {'service': serv}
    return render(request, 'horse/service_detail.html', {'service': serv, 'comments': comments, 'form': form})


