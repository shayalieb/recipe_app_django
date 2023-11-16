
from django.urls import path, include
from . import views
from .views import RecipeListView, RecipeDetailView, search_view
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    # path('recipes/', include('recipes.urls')),
    path('recipes/', RecipeListView.as_view(), name='recipes_list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('search/', search_view, name='search'),
]
