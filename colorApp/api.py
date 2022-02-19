from django.db.models import Q
from rest_framework import generics, permissions
from colorApp import models, serializers


class CreatePaletteView(generics.ListCreateAPIView):
    """
    Create Palette and view palette
    """
    serializer_class = serializers.CreatePaletteSerializer
    permission_classes = [permissions.IsAuthenticated]
    # queryset = models.PaletteModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return models.PaletteModel.objects.filter(user=self.request.user)


class SearchPaletteView(generics.ListAPIView):
    """
    Search Palette
    """
    serializer_class = serializers.CreatePaletteSerializer

    def get_queryset(self):
        keywords = self.request.query_params.get('search')
        try:
            queryset = models.PaletteModel.objects.filter(
                Q(palette_name__icontains=keywords) | Q(primary_one__icontains=keywords) | Q(
                    primary_two__icontains=keywords) | Q(secondary_one__icontains=keywords) | Q(
                    secondary_two__icontains=keywords) | Q(secondary_three__icontains=keywords) | Q(
                    secondary_four__icontains=keywords), public=True)
        except:
            queryset = models.PaletteModel.objects.all()
        return queryset


class AddFavouriteView(generics.ListCreateAPIView):
    """
    Add to Favourite (Un used)
    """
    serializer_class = serializers.AddFavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return models.FavouriteModel.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        current_palette = models.PaletteModel.objects.get(id=self.request.POST['palette'])
        try:
            current_favourite = models.FavouriteModel.objects.get(user=self.request.user, palette=current_palette)
            current_favourite.delete()
        except:
            favourite = models.FavouriteModel.objects.create(user=self.request.user, palette=current_palette)
            favourite.save()
