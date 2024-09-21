
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form-recipe/', views.form_recipe, name='form_recipe'),
    path('view-recipe/', views.view_recipes, name='view_recipes'),
    path('delete-recipe/<id>/', views.delete_recipe, name='delete_recipe'),
    path('update-recipe/<id>/', views.update_recipe, name='update_recipe')
]