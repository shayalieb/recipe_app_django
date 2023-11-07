from django.contrib import admin

# Import the recipes model
from .models import recipes 

# Register the models
admin.site.register(recipes)