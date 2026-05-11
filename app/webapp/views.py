from django.shortcuts import render

from django.http import HttpResponse

def welcome(request):
    return render(request, "welcome.html")

def product(request):
    return render(request, "product.html")

def contact(request):
    return render(request, "contact.html")

from django.shortcuts import redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)                    # Auto login after registration
            return redirect('welcome')              # or 'home'
        else:
            # If form has errors, show them
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'registration/profile.html', {
        'user': request.user
    })
