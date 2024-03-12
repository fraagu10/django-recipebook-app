from django.shortcuts import render
from django.utils import timezone
from .models import Recipe

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all().order_by('created_date')
    return render(request, 'recipebook/recipe_list.html', {'recipes': recipes})
