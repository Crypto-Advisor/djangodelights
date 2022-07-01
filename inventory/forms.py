from dataclasses import fields
from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

#create
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"


#update
class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'unit', 'quantity', 'price_per_unit')


class MenuItemUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('name', 'price')


class RecipeRequirementUpdateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menu_item', 'ingredient', 'quantity')


class PurchaseUpdateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('menu_item', 'quantity')

