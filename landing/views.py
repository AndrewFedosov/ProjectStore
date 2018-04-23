from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

def landing(reguest):
    form = SubscriberForm(reguest.POST or None)
    if reguest.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(reguest, 'landing/landing.html', locals())

def home(reguest):
    products_images = Product_image.objects.filter(is_active=True, is_main=True)
    return render(reguest, 'landing/home.html', locals())