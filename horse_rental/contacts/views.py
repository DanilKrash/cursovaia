from django.shortcuts import render
from contacts.models import Feedback
from contacts.forms import FeedbackForm


def contacts_view(request):
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
    return render(request, 'contacts/about_us.html', {'contact': cont, 'form': form})
