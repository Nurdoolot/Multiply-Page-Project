from django.shortcuts import render
from django.views.generic import ListView
from .models import Images


def home(request):
    return render(request, 'home/home.html')


def about(request):
    with open('D:\ptn-2\home\page/about.txt', 'r') as f:
        about = f.read()
    return render(request, 'home/about.html', {'about': about})


def contacts(request):
    with open('D:\ptn-2\home\page/contacts.txt', 'r') as f:
        contacts = f.read()
    return render(request, 'home/contacts.html', {'contacts': contacts})

class ImagesView(ListView):
    model = Images
    template_name = 'home/images.html'
    context_object_name = 'images'
