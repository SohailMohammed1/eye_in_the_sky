from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OFh3HHAgoExX0K4wJEubBV50fyRhZoZAB7TOFeCG43sFHkcK0pRa2N1tF14IZ27m3A93MX7WDthKxPwvh1UVPD60069LClVqa',
        'client_secret': 'test client secret', 
    }

    return render(request, template, context)
