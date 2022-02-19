from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class PaletteModel(models.Model):
    """
    Color Palette Model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='palette_user')
    palette_name = models.CharField(max_length=255)
    primary_one = models.CharField(max_length=255)
    primary_two = models.CharField(max_length=255)
    secondary_one = models.CharField(max_length=255)
    secondary_two = models.CharField(max_length=255)
    secondary_three = models.CharField(max_length=255)
    secondary_four = models.CharField(max_length=255)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.palette_name


class FavouriteModel(models.Model):
    """
    Favourite Palette Model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_user')
    palette = models.ForeignKey(PaletteModel, on_delete=models.CASCADE, related_name='favourite_palette')
