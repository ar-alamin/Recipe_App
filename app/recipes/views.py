from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')

def form_recipe(request):
    if request.method == "POST":  
        data = request.POST    
        recipe_name = data.get('recipe_name')
        recipe_des = data.get('recipe_des')
        recipe_img = request.FILES.get('recipe_img')

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_des = recipe_des,
            recipe_img = recipe_img,
        )
    return render(request, 'recipes/form_recipe.html')

def view_recipes(request):
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    return render(request, 'recipes/view_recipes.html', {'recipes': queryset})

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/view-recipe/')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        recipe_des = request.POST.get('recipe_des')
        recipe_img = request.FILES.get('recipe_img')

        queryset.recipe_name = recipe_name
        queryset.recipe_des = recipe_des

        if recipe_img:
                queryset.recipe_img = recipe_img
                
        queryset.save()
        return redirect('/view-recipe/')

    return render(request, 'recipes/update_recipe.html', {'recipe': queryset})
