from django.contrib import admin
from .models import FoodMenuItem, SideOption, AddedOption, SizeOption, GravyOption, CookOption, SauceOption, RemoveOption, Order, LineItem, MenuOption, DietaryOption, FoodPhoto

admin.site.register(FoodMenuItem)
admin.site.register(SideOption)
admin.site.register(AddedOption)
admin.site.register(SizeOption)
admin.site.register(GravyOption)
admin.site.register(CookOption)
admin.site.register(SauceOption)
admin.site.register(RemoveOption)
admin.site.register(Order)
admin.site.register(LineItem)
admin.site.register(MenuOption)
admin.site.register(DietaryOption)
admin.site.register(FoodPhoto)