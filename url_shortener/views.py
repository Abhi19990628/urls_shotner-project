from django.shortcuts import render, redirect
from .forms import URLForm
from .models import URL
import random
import string

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(6))
    return short_url

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_url = generate_short_url()
            url_obj = URL.objects.create(original_url=original_url, short_url=short_url)
            return render(request, 'url_shortener/home.html', {'form': form, 'url_obj': url_obj})
    else:
        form = URLForm()
    return render(request, 'url_shortener/home.html', {'form': form})

def redirect_original(request, short_url):
    url_obj = URL.objects.get(short_url=short_url)
    return redirect(url_obj.original_url)


