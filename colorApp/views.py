from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy

from colorApp import forms, models


# Create your views here.

# Create your views here.
def login_executed(redirect_to):
    """This Decorator kicks authenticated user out of a view"""

    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


def indexView(request):
    context = {}
    return render(request, 'index.html', context)


@login_required
def myPaletteView(request):
    """
    User created palettes
    """
    context = {}
    return render(request, 'my-palettes.html', context)


@login_required
def addFavouriteView(request, id):
    """
    Let user add palette to favourite
    """
    current_palette = models.PaletteModel.objects.get(id=id)
    try:
        current_favourite = models.FavouriteModel.objects.get(user=request.user, palette=current_palette)
        current_favourite.delete()
    except:
        favourite = models.FavouriteModel.objects.create(user=request.user, palette=current_palette)
        favourite.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def savedPaletteView(request):
    """
    Show Users saved palettes
    """
    saved_palettes = models.FavouriteModel.objects.filter(user=request.user)
    context = {
        'saved_palettes': saved_palettes
    }
    return render(request, 'saved-palettes.html', context)


@login_executed('color_app:index')
def loginView(request):
    form = forms.LoginForm()
    next_page = request.GET.get('next')
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        form = forms.LoginForm(data=request.POST)
        user = authenticate(username=user_name, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if next_page:
                    return redirect(next_page)
                return HttpResponseRedirect(reverse('color_app:index'))

    context = {'form': form}
    return render(request, 'login.html', context)


@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('color_app:index'))
