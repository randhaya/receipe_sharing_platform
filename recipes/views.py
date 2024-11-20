import requests

from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipe_results(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_results.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def search_recipes(request):
    query = request.GET.get('q', '')

    if query:
        response = requests.get(f'http://127.0.0.1:5000/search?q={query}')

        results = response.json()
    else:
        results = []

    return render(request, 'recipes/search_results.html', {'results': results})
