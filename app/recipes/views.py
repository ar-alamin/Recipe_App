from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')

# handle form 
@login_required(login_url="/login/")
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

# view recipe
def view_recipes(request):
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    return render(request, 'recipes/view_recipes.html', {'recipes': queryset})

# delete recipe
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/view-recipe/')

# update recipe
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


# handle login page
def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Credential!")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Invalid Credential!")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'recipes/login.html')

# handle logout page
def logout_page(request):
    logout(request)
    return redirect('/login')

# handle register page
def register(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "username exists")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Account successfully created!")

        return redirect('/register/')

    return render(request, 'recipes/register.html')