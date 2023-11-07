# imported by default
from django.shortcuts import render
# This will allow the list to be displayed as a list, and the detail to be displayed as a detail
from django.views.generic import ListView, DeleteView
#import the model
from .models import recipes
from django.contrib.auth.mixins import LoginRequiredMixin

# define the home view here - function based view
def home(request):
    return render(request, 'recipes/recipes_home.html')

# Create the recipe list view here - Class based view
class RecipeListView(LoginRequiredMixin, ListView):
    model = recipes
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('recipes')
        if q:
            return queryset.filter(name__icontains=q)
        return queryset

# Recipe detail view here - class based view
class RecipeDetailView(LoginRequiredMixin, DeleteView):
    model = recipes
    template_name = 'recipes/recipes_detail.html'
    context_object_name = 'recipes_detail'
    ordering = ['name']

class RecipeSearchView(LoginRequiredMixin, ListView):
    model = recipes
    template_name = 'recipes/recipe_search.html'

    def get_queryset(self):
        query = self.request.GET.get('recipes')
        if query:
            return recipes.objects.filter(name__icontains=query)
        return recipes.objects.all()