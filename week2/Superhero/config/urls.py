from django.urls import path
from hero.views import IndexView, TheFlashView, GreenArrowView

urlpatterns = [
    path('', IndexView.as_view()),
    path('greenarrow', GreenArrowView.as_view()),
    path('theflash', TheFlashView.as_view()),
]