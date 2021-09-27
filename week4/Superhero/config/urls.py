from django.urls import path
from hero.views import IndexView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
]