from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),

    path('menu/food/', views.FoodMenuItemList.as_view(), name='food_menu'),
    path('menu/food/create/', views.FoodMenuItemCreate.as_view(), name='food_menu_item_create'),
    path('menu/food/<int:pk>/', views.FoodMenuItemDetail.as_view(), name='food_menu_item_detail'),
    path('menu/food/<int:pk>/add_to_order', views.create_line_item, name='add_line_item'),
    path('menu/food/<int:foodmenuitem_id>/add_food_photo/', views.add_food_photo, name='add_food_photo'),
    path('menu/food/<int:pk>/update/', views.FoodMenuItemUpdate.as_view(), name='food_menu_item_update'),
    path('menu/food/<int:pk>/delete/', views.FoodMenuItemDelete.as_view(), name='food_menu_item_delete'),

    path('menu/drinks/', views.DrinkMenuItemList.as_view(), name='drink_menu'),
    path('menu/drinks/create/', views.DrinkMenuItemCreate.as_view(), name='drink_menu_item_create'),
    path('menu/drinks/<int:pk>/', views.DrinkMenuItemDetail.as_view(), name='drink_menu_item_detail'),
    path('menu/drinks/<int:pk>/update/', views.DrinkMenuItemUpdate.as_view(), name='drink_menu_item_update'),
    path('menu/drinks/<int:pk>/delete/', views.DrinkMenuItemDelete.as_view(), name='drink_menu_item_delete'),

    path('menu/order/create', views.create_order, name='order_create'),
    path('menu/order/view', views.view_order, name='order_view'),

    path('event/', views.EventList.as_view(), name='event_list'),
    path('event/add_event', views.EventCreate.as_view(), name='event_create'),
    path('event/<int:pk>/', views.EventDetail.as_view(), name='event_detail'),
    path('event/<int:event_id>/add_event_photo/', views.add_event_photo, name='add_event_photo')
]