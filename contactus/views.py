from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ContactForm
from .forms import ContactUsForm

from checkout.models import Order


def contact(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "We've sent your contact form and will be in touch soon")
        else:
            messages.error(equest, "Oh no, something went wrong! Please check the form.")
    else:
        form = ContactUsForm(instance=profile)

    template = 'profiles/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

