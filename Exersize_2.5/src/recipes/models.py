from django.db import models
from django.shortcuts import reverse

class recipes(models.Model):
    pic = models.ImageField(upload_to='recipes', default='no_image.svg')
    name = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=500)  
    cooking_time = models.IntegerField()
    instructions = models.TextField()

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(',')
        if self.cooking_time < 30 and len(ingredients) < 6:
            return 'Easy'
        elif self.cooking_time < 30 and len(ingredients) >= 6:
            return 'Medium'
        elif self.cooking_time >= 30 and len(ingredients) < 6:
            return 'Intermediate'
        elif self.cooking_time >= 30 and len(ingredients) >= 6:
            return 'Hard'
        return 'difficulty'
    
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('recipes-detail', kwargs={'pk': self.pk})