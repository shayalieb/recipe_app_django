from django import forms
from django.shortcuts import render
from .models import recipes


CHART_CHOICES = (
    ('1', 'Pie Chart'),
    ('2', 'Bar Chart'),
    ('3', 'Line Chart'),
)


class SearchForm(forms.Form):
    query = forms.CharField()

    def search_view(self, request):
        form = SearchForm(request.POST) if request.method == 'POST' else SearchForm(None)

        results = []
        if form.is_valid():
            query = form.cleaned_data['query']
            results = recipes.objects.filter(name=query) # adjust this line to match your search criteria

        return render(request, 'search_results.html', {'results': results})