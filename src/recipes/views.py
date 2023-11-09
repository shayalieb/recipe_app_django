# imported by default
from django.shortcuts import render
# This will allow the list to be displayed as a list, and the detail to be displayed as a detail
from django.views.generic import ListView, DeleteView
#import the model
from .models import recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm

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
        if (q := self.request.GET.get('recipes')):
            return queryset.filter(name__icontains=q)
        return queryset

# Recipe detail view here - class based view
class RecipeDetailView(LoginRequiredMixin, DeleteView):
    model = recipes
    template_name = 'recipes/recipes_detail.html'
    context_object_name = 'recipes_detail'
    ordering = ['name']


def search_view(request):
    #create an instance of SalesSearchForm that you defined in sales/forms.py
    form = SearchForm(request.POST or None)
    #name = None

    #check if the button is clicked
    if request.method =='POST':
        name = request.POST.get('name', '')
        chart_type = request.POST.get('chart_type', '1')
    # process the name and chart_type here
    # then return a HttpResponse
        return render(request, 'your_template.html', {'name': name, 'chart_type': chart_type})

    print ('Exploring querysets:')
    print ('Case 1: Output of recipes.objects.all()')
    qs = recipes.objects.filter(name)
    print (qs)

    print ('Case 2: Output of Sale.objects.filter(book_name=book_title)')
    qs = recipes.objects.filter(recipes=name)
    print (qs)

    print ('Case 3: Output of qs.recipes')
    print (qs.values())

    print ('Case 4: Output of qs.v(recipes_list)')
    print (qs.values_list())

    print ('Case 5: Output of recipes.objects.get(id=1)')
    obj = recipes.objects.get(id=1)
    print (obj)

   #pack up data to be sent to template in the context dictionary
    context={
            'form': form,
    }

   #load the sales/record.html page using the data that you just prepared
    return render(request, 'sales/search.html', context)