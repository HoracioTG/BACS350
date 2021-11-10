from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    RedirectView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.base import TemplateView


from .models import Hero


class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Hero


class HeroDetailView(TemplateView):
    template_name = "hero_detail.html"
    model = Hero

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Hero.objects.get(pk=hero_id)
        return {'hero': hero}


class HeroView(TemplateView):
    model= Hero
    template_name= 'index.html'


class HeroCreateView(CreateView):
    template_name = "hero_add.html"
    model = Hero
    fields = ["name", "description", "identity", "weakness", "strength", "image"]


class HeroUpdateView(UpdateView):
    template_name = "hero_edit.html"
    model = Hero
    fields = ["name", "description", "identity", "weakness", "strength", "image"]


class HeroDeleteView(DeleteView):
    template_name = "hero_delete.html"
    success_url = reverse_lazy("hero_list")
    model = Hero


# Create your views here.
