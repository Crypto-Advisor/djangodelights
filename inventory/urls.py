from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', include('django.contrib.auth.urls'), name="login"),

    path('ingredient/', views.IngredientList.as_view(), name="ingredientlist"),

    path('ingredient/create', views.IngredientCreate.as_view(), name="ingredientcreate"),
    path('menuitem/create', views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path('recipe/create', views.RecipeRequirementCreate.as_view(), name="recipecreate"),
    path('purchase/create', views.PurchaseCreate.as_view(), name="purchasecreate"),

    path('ingredient/update/<pk>', views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path('menuitem/update/<pk>', views.MenuItemUpdate.as_view(), name="menuitemupdate"),
    path('recipe/update/<pk>', views.RecipeRequirementUpdate.as_view(), name="recipeupdate"),
    path('purchase/update/<pk>', views.PurchaseUpdate.as_view(), name="purchaseupdate"),

    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name="ingredientdelete"),
    path('menuitem/delete/<pk>', views.MenuItemDelete.as_view(), name="menuitemdelete"),
    path('recipe/delete/<pk>', views.RecipeRequirementDelete.as_view(), name="recipedelete"),
    path('purchase/delete/<pk>', views.PurchaseDelete.as_view(), name="purchasedelete"),
]