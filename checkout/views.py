from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oh no, you don't have anything to buy!")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ND9nGDPceoUBZbJmMMCM67nAac7cGhDAO2Gt4M4DmMcMS4FbtxsJNTC4XvTqerPCByw0QJdP5ePXOUn64hofIZW00MutSyB0o',
        'client_secret': 'test client key',
    }

    return render(request, template, context)