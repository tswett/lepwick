from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import UserHolding

def index(request):
    all_holdings = UserHolding.objects.all()
    template = loader.get_template('mainapp/index.html')
    context = { 'holdings': all_holdings }

    return HttpResponse(template.render(context, request))
