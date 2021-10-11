from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import Hero

class HeroListView(ListView):
    template_name = 'hero_list.html'
    model = Hero

class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = Hero

class IndexView(TemplateView):
    model = Hero
    template_name = 'index.html'



# Create your views here.
