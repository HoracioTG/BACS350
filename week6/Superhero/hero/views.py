from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView


from .models import Hero



class HeroListView(ListView):
    template_name = 'hero_list.html'
    model = Hero

class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = Hero

class HeroView(RedirectView):
    url = '/hero/'

class HeroCreateView(CreateView):
    template_name = 'hero_add.html'
    model = Hero
    fields = ['name', 'description']

class HeroUpdateView(UpdateView):
    template_name = 'hero_edit.html'
    model = Hero
    fields = ['name', 'description']

class HeroDeleteView(DeleteView):
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('book_list')



# Create your views here.
