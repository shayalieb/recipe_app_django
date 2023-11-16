# Import libraries for views.py and django form authentication
import matplotlib.pyplot as plt
import os
import io
import urllib, base64
from django.conf import settings

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
from django.shortcuts import redirect, render
from recipes.forms import SearchForm
from recipes.models import recipes

# When the user hits the LOGIN button the post request is
def login_view(request: HttpRequest):
    error_message = None
    form  = AuthenticationForm()
    context = {'form': form, 'error_message': error_message}  # Initialize context here

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            #Django authentication function
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes:home')
        else:
            error_message = 'Invalid username or password'
            context = {'form': form, 'error_message': error_message}
    return render(request, 'login.html', context)

def generate_plots():
    fig, ax = plt.subplots()
    ax.bar(...)  # Fill in with your data
    fig.savefig(os.path.join(settings.STATIC_ROOT, 'bar_plot.png'))

    fig, ax = plt.subplots()
    ax.pie(...)  # Fill in with your data
    fig.savefig(os.path.join(settings.STATIC_ROOT, 'pie_plot.png'))

    fig, ax = plt.subplots()
    ax.plot(...)  # Fill in with your data
    fig.savefig(os.path.join(settings.STATIC_ROOT, 'line_plot.png'))

def process_search_form(form):
    return recipes.objects.filter(name__icontains=form.cleaned_data.get('search_term'))    

def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            results = process_search_form(form)
            generate_plots()
            return render(request, 'search.html', {
                'form': form, 
                'results': results,
                'bar_plot': 'bar_plot.png',
                'pie_plot': 'pie_plot.png',
                'line_plot': 'line_plot.png',
            })
    else:
        form = SearchForm()
        return render(request, 'search.html', {'form': form})

def plot_view(request):
    generate_plots()  # This will generate the plot image
    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)
    image_url = urllib.parse.quote(base64.b64encode(image.read()))
    return render(request, 'search.html', {'image_url': image_url})

def logout_view(request: HttpRequest):
    logout(request)
    return redirect('logout_success')

def logout_success(request):
    return render(request, 'success.html')
