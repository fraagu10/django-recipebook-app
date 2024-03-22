from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from .models import Recipe
from .forms import RecipeForm


# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all().order_by('created_date')
    return render(request, 'recipe_list/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_list/recipe_detail.html', {'recipe': recipe})

def recipedia_home(request):
    return render(request, "recipe_list/home.html", {})

def recipe_new(request):
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author_name = request.user 
            recipe.created_date = timezone.now()
            recipe.last_updated = timezone.now()
            recipe.save()

            return redirect('recipe_detail', pk=recipe.pk)
    
    return render(request, "recipe_list/recipe_add.html", {'form': form})
