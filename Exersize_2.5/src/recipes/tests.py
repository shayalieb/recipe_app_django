from django.test import TestCase, Client
from django.urls import reverse
from .models import recipes
from .views import RecipeListView, RecipeDetailView


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        recipes.objects.create(name='Rice', cooking_time=40, ingredients='rice, water, salt', instructions='boil water, add rice, add salt, cook for 40 minutes')

    def test_name_label(self):
        recipe = recipes.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_ingredients_label(self):
        recipe = recipes.objects.get(id=1)
        field_label = recipe._meta.get_field('ingredients').verbose_name
        self.assertEquals(field_label, 'ingredients')

    def test_cooking_time_label(self):
        recipe = recipes.objects.get(id=1)
        field_label = recipe._meta.get_field('cooking_time').verbose_name
        self.assertEquals(field_label, 'cooking time')

    def test_instructions_label(self):
        recipe = recipes.objects.get(id=1)
        field_label = recipe._meta.get_field('instructions').verbose_name
        self.assertEquals(field_label, 'instructions')

    def test_name_max_length(self):
        recipe = recipes.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

