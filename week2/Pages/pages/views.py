from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Index page', 
            'body': 'AyoooooO',
        }

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

