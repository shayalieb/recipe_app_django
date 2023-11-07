
from django.urls import path
from . import views
from .views import RecipeListView, RecipeDetailView
from django.urls import path

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('recipes/', RecipeListView.as_view(), name='recipes-list'),
#      path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
# ]
urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', RecipeListView.as_view(), name='recipes_list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/search/', views.RecipeSearchView.as_view(), name='recipe_search'),
]
