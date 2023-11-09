from django.db import models

# Class for the recipes app
class recipes(models.Model):
    pic = models.ImageField(upload_to='recipes', default='no_image.svg')
    name = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=500)  
    cooking_time = models.IntegerField()
    instructions = models.TextField()
    
    #cConfigure the difficulty level to be shown in the main user side
    def calculate_difficulty(self):
        ingredients = self.ingredients.split(',')
        if self.cooking_time < 30:
            return 'Easy' if len(ingredients) < 6 else 'Medium'
        else:
            return 'Intermediate' if len(ingredients) < 6 else 'Hard'
    
    def __str__(self):
        return str(self.name)