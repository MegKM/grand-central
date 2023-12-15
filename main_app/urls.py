from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('menu/', views.FoodMenuItemList.as_view(), name='food_menu'),
  path('menu/food/create', views.FoodMenuItemCreate.as_view(), name='food_menu_item_create'),
  path('menu/food/<int:pk>/', views.FoodMenuItemDetail.as_view(), name='food_menu_item_detail'),

]