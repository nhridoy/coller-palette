from django.urls import path
from colorApp import views, api

app_name = 'color_app'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('my-palette/', views.myPaletteView, name='my-palette'),
    path('saved-palette/', views.savedPaletteView, name='saved-palette'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('favourite/', views.addFavouriteView, name='favourite'),
    path('favourite/<id>/', views.addFavouriteView, name='favourite'),

    # Api
    path('create-palette/', api.CreatePaletteView.as_view(), name='create-palette'),
    path('search-palette/', api.SearchPaletteView.as_view(), name='search-palette'),
    path('add-favourite/', api.AddFavouriteView.as_view(), name='add-favourite'),
]