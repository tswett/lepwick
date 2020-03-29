from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Recipe, UserHolding

def index(request):
    all_holdings = UserHolding.objects.all()
    all_recipes = Recipe.objects.all()
    template = loader.get_template('mainapp/index.html')
    context = { 'holdings': all_holdings, 'recipes': all_recipes }

    return HttpResponse(template.render(context, request))

def do_recipe(request):
    recipe_id = int(request.POST['recipe'])
    recipe = Recipe.objects.get(pk=recipe_id)
    inventory = request.user.userinventory

    recipe.execute_for(inventory)

    return HttpResponse('You have successfully executed this recipe.', content_type='text/plain')
