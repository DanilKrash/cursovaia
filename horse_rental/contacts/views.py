from django.shortcuts import render


def contacts_view(request):
    return render(request, 'contacts/about_us.html')
