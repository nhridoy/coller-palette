from rest_framework import serializers
from colorApp import models


class CreatePaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaletteModel
        fields = '__all__'
        extra_kwargs = {
            'user': {
                'read_only': True
            }
        }


class AddFavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavouriteModel
        fields = '__all__'
        extra_kwargs = {
            'user': {
                'read_only': True
            }
        }
