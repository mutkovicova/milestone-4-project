from django.shortcuts import render

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oh no, you don't have anything to buy!")
        return redirect(reverse('products'))
