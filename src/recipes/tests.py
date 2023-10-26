from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import recipes

# Test class for the "recipes" model
class RecipeModelTest(TestCase):
    recipes.objects.create(
        name='Rice', 
        cooking_time=40, 
        ingredients='rice, water, salt',
        instructions='boil water, add rice, add salt, cook for 40 minutes',
    )

    # Test that the recipe name is correct
    def test_recipe_name(self):
        recipe = recipes.objects.get(id=1)
        recipe_name_label = recipe._meta.get_field('name').verbose_name
        self.assertEquals(recipe_name_label, 'name')

    # Test cooking_time is an integer and has the correct response
    def test_cooking_time_helptext(self):
        recipe = recipes.objects.get(id=1)
        recipe_cooking_time = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(recipe_cooking_time, 'in minutes')


  


        