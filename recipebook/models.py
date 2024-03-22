from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=90)
    description = models.TextField(max_length=240)
    number_of_servings = models.IntegerField()
    prep_time = models.PositiveSmallIntegerField()
    cook_time = models.PositiveSmallIntegerField()
    # total_time = models.IntegerField()
    ingredients = models.TextField(blank=True)
    cooking_instructions = models.JSONField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    notes = models.TextField(max_length=360, blank=True)
    substitutions = models.TextField(blank=True)

    def update(self):
        self.last_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.title
