
from django.urls import path
from . import views
from .views import RecipeListView, RecipeDetailView, RecipeSearchForm
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
    path('search/', records, name='recipe_search'),
]
