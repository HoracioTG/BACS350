from django.views.generic import TemplateView

class GreenArrowView(TemplateView):
    template_name = 'greenarrow.html'

    

class TheFlashView(TemplateView):
    template_name = "theflash.html"
