from django.shortcuts import render
from .forms import SubscriberForm

def landing(reguest):
    form = SubscriberForm(reguest.POST or None)
    if reguest.method == "POST" and form.is_valid():
        print (reguest.POST)
        print(form.cleaned_data)

        new_form = form.save()

    return render(reguest, 'landing/landing.html', locals())