from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search_recipes, name='search_recipes'),
    path('', views.recipe_results, name='recipe_results'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
]