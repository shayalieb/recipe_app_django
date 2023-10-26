from django.contrib import admin

# Import the recipes model
from .models import recipes 

# Input recipe data into the admin page
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'cooking_time', 'instructions', 'difficulty', 'calculate_difficulty')
# Register your models here.
admin.site.register(recipes)
