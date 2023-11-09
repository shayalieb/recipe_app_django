from django import forms
from django.views import View

CHART_CHOICES = (
    ('1', 'Pie Chart'),
    ('2', 'Bar Chart'),
    ('3', 'Line Chart'),
)

class RecipeSearchForm(View):
    search_term = forms.CharField(max_length=100, label='Search Recipes')
    chart_type = forms.ChoiceField(choices=CHART_CHOICES, label='Chart Type')