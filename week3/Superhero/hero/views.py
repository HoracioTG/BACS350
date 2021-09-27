from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My index page', 
            'body': <a href="/http://127.0.0.1:8000/greenarrow">Green Arrow</a> <a href="/http://127.0.0.1:8000/theflash">The Flash</a> 
            ,
        }

class TheFlashView(TemplateView):
    template_name = "theflash.html"
    def get_context_data(self, **kwargs):
        return {
            'title': 'The Flash', 
            'body': 'Create content for The Flash',
        }

class GreenArrowView(TemplateView):
    template_name = "greenarrow.html"
    def get_context_data(self, **kwargs):
        return {
            'title': 'Green Arrow', 
            'body': 'Create content for Green Arrow',
        }