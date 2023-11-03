
from django.urls import path
from . import views
from .views import RecipeListView
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', RecipeListView.as_view(), name='recipes-list'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipes-detail'),
]

