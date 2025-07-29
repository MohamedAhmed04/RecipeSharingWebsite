# recipes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm

def recipe_list(request):
    """
    Display all recipes ordered by creation date.
    """
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, id):
    """
    Display detailed information for a single recipe.
    """
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    """
    Handle the submission of a new recipe via the frontend form.
    """
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            # Redirect to the recipe detail page after successful submission
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})
