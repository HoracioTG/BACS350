from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My about page', 
            'body': 'AyoooooO',
        }

class HomeView(TemplateView):
    template_name = "home.html"

class IndexView(TemplateView):
    template_name = "index.html"

