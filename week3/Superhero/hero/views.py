from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My index page', 
            'body': 'AyoooooO',
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