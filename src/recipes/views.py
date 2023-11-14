# imported by default
from django.shortcuts import render
# This will allow the list to be displayed as a list, and the detail to be displayed as a detail
from django.views.generic import ListView, DeleteView
#import the model
from .models import recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm
from django.db.models import Q
# from django.http import HttpResponseRedirect

# define the home view here - function based view
def home(request):
    return render(request, 'recipes/recipes_home.html')

# Create the recipe list view here - Class based view

class RecipeListView(LoginRequiredMixin, ListView):
    model = recipes
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context
    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if not form.is_valid():
            return super().get(request, *args, **kwargs)

        name_query = form.cleaned_data['search_term']
        # ingredients_query = form.cleaned_data['ingredients']
        self.object_list = self.model.objects.filter(name__icontains=name_query)
        # self.object_list = self.model.objects.filter(name__icontains=ingredients_query)
        context = self.get_context_data(object_list=self.object_list, form=form)
        return render(request, self.template_name, context)
# Recipe detail view here - class based view
class RecipeDetailView(LoginRequiredMixin, DeleteView):
    model = recipes
    template_name = 'recipes/recipes_detail.html'
    context_object_name = 'recipes_detail'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context
    
    


def search_view(request):
    form = SearchForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        if name:
            results = recipes.objects.filter(name__icontains=name) if name else []
        else:
            results = []
        if results:
            message = "Results:" if results else f"Recipe '{name}' not found."
        else:
            message = f"Recipe '{name}' not found."

        return render(request, 'search.html', {'form': form, 'results': results, 'message': message})

    return render(request, 'search.html', {'form': form})