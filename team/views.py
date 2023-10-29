from django.shortcuts import render
from .models import Team

# Create your views here.


def view_team_list(request):
    team = Team.objects.all()
    template = 'team/team_list.html'
    context = {
        'team': team
    }
    return render(request, template, context)
