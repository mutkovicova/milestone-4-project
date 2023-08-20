from django.shortcuts import render, redirect
from slovak_shop.forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('contact-success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
    messages.success(request, "We've got your note!")
    return render(request, 'contact-success.html')
