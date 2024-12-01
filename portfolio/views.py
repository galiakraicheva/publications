from django.shortcuts import render
from .models import Publication

def about_me(request):
    publications = Publication.objects.all().order_by('-date_posted')
    context = {
        'publications': publications,
    }
    return render(request, 'portfolio/about_me.html', context)

def publications(request):
    publications = Publication.objects.all().order_by('-date_posted')
    return render(request, 'portfolio/publications.html', {'publications': publications})

def contact(request):
    return render(request, 'portfolio/contact.html')

