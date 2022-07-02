from audioop import reverse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm, IngredientUpdateForm, MenuItemUpdateForm, RecipeRequirementUpdateForm, PurchaseUpdateForm

# Create your views here.
@login_required
def home(request):
    context = {"name": request.user}
    return render(request, 'inventory/home.html', context)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def logout_view(request):
    logout(request)
    return redirect('login')

# read
class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'inventory/inventory.html'

class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'

class RecipeRequirementList(LoginRequiredMixin, ListView):
    model = RecipeRequirement
    template_name = 'inventory/recipies.html'

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'inventory/purchases.html'

#create
class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_create_form.html'
    form_class = IngredientForm

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = 'inventory/menu_item_create_form.html'
    form_class = MenuItemForm

class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_create_form.html'
    form_class = RecipeRequirementForm

class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = 'inventory/purchase_create_form.html'
    form_class = PurchaseForm

#update
class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_update_form.html'
    form_class = IngredientUpdateForm

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = 'inventory/menu_item_update_form.html'
    form_class = MenuItemUpdateForm

class RecipeRequirementUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_update_form.html'
    form_class = RecipeRequirementUpdateForm

class PurchaseUpdate(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = 'inventory/purchase_update_form.html'
    form_class = PurchaseUpdateForm


#delete
class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'
    success_url = '/ingredient'

class MenuItemDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'inventory/menu_item_delete_form.html'
    success_url = ''

class RecipeRequirementDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_delete_form.html'
    success_url = ''

class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = 'inventory/purchase_delete_form.html'
    success_url = ''
