from django.shortcuts import render


def main(request):
    return render(request, 'horse/main.html')


def about(request):
    return render(request, 'horse/about.html')
