from django import forms
from django.shortcuts import render
from .models import recipes


CHART_CHOICES = (
    ('1', 'Pie Chart'),
    ('2', 'Bar Chart'),
    ('3', 'Line Chart'),
)


class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=200, required=False, label="Search Recipes")
    # ingredients = forms.CharField(max_length=200, required=False)
    show_all = forms.BooleanField(required=False)
    

class RecipeSearchForm(forms.Form):
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)

