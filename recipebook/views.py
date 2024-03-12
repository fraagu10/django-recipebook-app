from django.shortcuts import render

# Create your views here.
def recipe_list(request):
    return render(request, 'recipebook/recipe_list.html', {})
