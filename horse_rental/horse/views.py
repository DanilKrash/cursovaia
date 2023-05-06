from django.shortcuts import render


def main(request):
    return render(request, 'horse/main.html')


def service(request):
    return render(request, 'horse/service.html')


def contact(request):
    return render(request, 'horse/contact.html')
