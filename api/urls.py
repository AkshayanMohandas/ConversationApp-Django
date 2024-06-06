from django.urls import path
from .views import index_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('index/', index_view, name='index'),
]
