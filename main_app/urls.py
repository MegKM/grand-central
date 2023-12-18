from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/food/', views.FoodMenuItemList.as_view(), name='food_menu'),
    path('menu/food/create/', views.FoodMenuItemCreate.as_view(), name='food_menu_item_create'),
    path('menu/food/<int:pk>/', views.FoodMenuItemDetail.as_view(), name='food_menu_item_detail'),
    path('menu/food/<int:foodmenuitem_id>/add_photo/', views.add_photo, name='add_photo'),
    path('menu/food/<int:pk>/update/', views.FoodMenuItemUpdate.as_view(), name='food_menu_item_update'),
    path('menu/food/<int:pk>/delete/', views.FoodMenuItemDelete.as_view(), name='food_menu_item_delete'),
    path('menu/drinks/', views.DrinkMenuItemList.as_view(), name='drink_menu'),
    path('menu/drinks/create/', views.DrinkMenuItemCreate.as_view(), name='drink_menu_item_create'),
    path('menu/drinks/<int:pk>/', views.DrinkMenuItemDetail.as_view(), name='drink_menu_item_detail'),
    path('menu/drinks/<int:pk>/update/', views.DrinkMenuItemUpdate.as_view(), name='drink_menu_item_update'),
    path('menu/drinks/<int:pk>/delete/', views.DrinkMenuItemDelete.as_view(), name='drink_menu_item_delete'),
]