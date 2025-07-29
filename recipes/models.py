# recipes/models.py

from django.db import models
from django.urls import reverse

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="A short description of the recipe")
    ingredients = models.TextField(help_text="List the ingredients")
    instructions = models.TextField(help_text="Step-by-step instructions")
    image_url = models.URLField(blank=True, null=True, help_text="URL of an image for the recipe")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Redirect to the recipe detail page after creation
        return reverse("recipe_detail", args=[str(self.id)])
