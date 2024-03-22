from django import forms

from .models import Recipe

class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'number_of_servings', 'prep_time', 'cook_time', 'ingredients', 'cooking_instructions','notes', 'substitutions')