from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('do_recipe', views.do_recipe, name='do_recipe'),
]
