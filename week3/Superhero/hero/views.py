from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My index page', 
            'body': 'Ayoooo',
            
        }

class TheFlashView(TemplateView):
    template_name = "theflash.html"
    def get_context_data(self, **kwargs):
        return {
            'title': 'The Flash', 
            'body': 'Create content for The Flash',
            'image': '/static/images/theflash.jpg',
        }

class GreenArrowView(TemplateView):
    template_name = "greenarrow.html"
    def get_context_data(self, **kwargs):
        return {
            'title': 'Green Arrow', 
            'body': 'Create content for Green Arrow',
            'image': '/static/images/greenarrow.jpg',
        }