from django.shortcuts import render
from .models import Partners

# Create your views here.


def view_partners_list(request):
    partners = Partners.objects.all()
    template = 'partners/partners_list.html'
    context = {
        'partners': partners
    }
    return render(request, template, context)
