from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oh no, you don't have anything to buy!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ND9nGDPceoUBZbJmMMCM67nAac7cGhDAO2Gt4M4DmMcMS4FbtxsJNTC4XvTqerPCByw0QJdP5ePXOUn64hofIZW00MutSyB0o',
        'client_secret': 'test client key',
    }

    return render(request, template, context)