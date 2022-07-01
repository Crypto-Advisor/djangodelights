from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm, IngredientUpdateForm, MenuItemUpdateForm, RecipeRequirementUpdateForm, PurchaseUpdateForm

# Create your views here.

def home(request):
    context = {"name": request.user}
    return render(request, 'inventory/home.html', context)

# read
class IngredientList(ListView):
    model = Ingredient

class MenuItemList(ListView):
    model = MenuItem

class RecipeRequirementList(ListView):
    model = RecipeRequirement

class PurchaseList(ListView):
    model = Purchase

#create
class IngredientCreate(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_create_form.html'
    form_class = IngredientForm

class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = 'inventory/menu_item_create_form.html'
    form_class = MenuItemForm

class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_create_form.html'
    form_class = RecipeRequirementForm

class PurchaseCreate(CreateView):
    model = Purchase
    template_name = 'inventory/purchase_create_form.html'
    form_class = PurchaseForm

#update
class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_update_form.html'
    form_class = IngredientUpdateForm

class MenuItemUpdate(UpdateView):
    model = MenuItem
    template_name = 'inventory/menu_item_update_form.html'
    form_class = MenuItemUpdateForm

class RecipeRequirementUpdate(UpdateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_update_form.html'
    form_class = RecipeRequirementUpdateForm

class PurchaseUpdate(UpdateView):
    model = Purchase
    template_name = 'inventory/purchase_update_form.html'
    form_class = PurchaseUpdateForm


#delete
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'
    success_url = '/ingredient'

class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = 'inventory/menu_item_delete_form.html'
    success_url = ''

class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_delete_form.html'
    success_url = ''

class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = 'inventory/purchase_delete_form.html'
    success_url = ''
