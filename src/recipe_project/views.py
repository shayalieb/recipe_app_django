# Import libraries for views.py and django form authentication
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm 
from django.http import HttpRequest
from django.shortcuts import redirect, render

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

