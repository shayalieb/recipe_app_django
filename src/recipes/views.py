# imported by default
from django.shortcuts import render
# This will allow the list to be displayed as a list, and the detail to be displayed as a detail
from django.views.generic import ListView, DeleteView
#import the model
from .models import recipes

# define the home view here - function based view
def home(request):
    return render(request, 'recipes/recipes_home.html')

# Create the recipe list view here - Class based view
class RecipeListView(ListView):
    model = recipes
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'
    ordering = ['name']

# Recipe detail view here - class based view
class RecipeDetailView(DeleteView):
    model = recipes
    template_name = 'recipes/recipes_detail.html'
    context_object_name = 'recipes_detail'
    ordering = ['name']