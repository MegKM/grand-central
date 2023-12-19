from django.db import models
from django.forms import FloatField, BooleanField, DecimalField
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class SideOption(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class AddedOption(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default = 0.0, decimal_places = 2, max_digits = 10)

    def __str__(self):
        return f'{self.name} - ${self.price}'
    
class SizeOption(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default = 0.0, decimal_places = 2, max_digits = 10)

    def __str__(self):
        return f'{self.name} - ${self.price}'

class GravyOption(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default = 0.0, decimal_places = 2, max_digits = 10)

    def __str__(self):
        return f'{self.name} - ${self.price}'

class CookOption(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    
    
class SauceOption(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RemoveOption(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name  
    
class CoffeeSizeOption(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default = 0.0, decimal_places = 2, max_digits = 10)

    def __str__(self):
        return f'{self.name} - ${self.price}'
    
class MilkOption(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default = 0.0, decimal_places = 2, max_digits = 10)

    def __str__(self):
        return f'{self.name} - ${self.price}'
    
class CoffeeStrengthOption(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SoftDrinkOption(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default = 0.0, decimal_places = 2, max_digits = 10)

    def __str__(self):
        return f'{self.name} - ${self.price}'

class HotChocolateOption(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class FoodMenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(default = 1.0, decimal_places = 2, max_digits = 10)
    inStock = models.BooleanField(default = True)    
    side_option = models.ManyToManyField(SideOption, help_text='Select all that apply', blank=True)
    added_option = models.ManyToManyField(AddedOption, help_text='Select all that apply', blank=True)
    size_option = models.ManyToManyField(SizeOption, help_text='Select all that apply', blank=True)
    gravy_option = models.ManyToManyField(GravyOption, help_text='Select all that apply', blank=True)
    cook_option = models.ManyToManyField(CookOption, help_text='Select all that apply', blank=True)
    sauce_option = models.ManyToManyField(SauceOption, help_text='Select all that apply', blank=True)
    remove_option = models.ManyToManyField(RemoveOption, help_text='Select all that apply', blank=True)

    def __str__(self):
        return self.name
            
    def size_calculation(self):
        result = []
        for size in self.size_option.all():
            total_price = self.price + size.price
            result.append({'name': size.name, 'price': total_price})
        print(result)
        return result
            
    def get_absolute_url(self):
        return reverse('food_menu_item_detail', kwargs={'pk': self.id})
    
class DrinkMenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(default = 1.0, decimal_places = 2, max_digits = 10)
    inStock = models.BooleanField(default = True)
    inhouse_option = models.BooleanField(default = False)
    coffee_size_option = models.ManyToManyField(CoffeeSizeOption, help_text='Select all that apply', blank=True)
    milk_option = models.ManyToManyField(MilkOption, help_text='Select all that apply', blank=True)
    coffee_strength_option = models.ManyToManyField(CoffeeStrengthOption, help_text='Select all that apply', blank=True)
    soft_drink_option = models.ManyToManyField(SoftDrinkOption, help_text='Select all that apply', blank=True)
    hot_chocolate_option = models.ManyToManyField(HotChocolateOption, help_text='Select all that apply', blank=True)
    
    def get_absolute_url(self):
        return reverse('drink_menu_item_detail', kwargs={'pk': self.id})
    
class Order(models.Model):
    date = models.DateField()
    total_price = models.FloatField(default = 1.0)
    notes = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='Guest')

    def __str__(self):
        return f'Order no. {self.id}'
    
    class Meta:
        ordering = ['-date']

class LineItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default = 0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(FoodMenuItem, on_delete=models.CASCADE)
    side_option = models.ManyToManyField(SideOption, help_text='Select all that apply', blank=True)
    size_option = models.ManyToManyField(SizeOption, help_text='Select all that apply', blank=True)
    cook_option = models.ManyToManyField(CookOption, help_text='Select all that apply', blank=True)
    sauce_option = models.ManyToManyField(SauceOption, help_text='Select all that apply', blank=True)
    remove_option = models.ManyToManyField(RemoveOption, help_text='Select all that apply', blank=True)

    def save(self, *args, **kwargs):
        if self.item:
            self.side_option.set(self.item.side_option.all())
        if self.item:
            self.added_option.set(self.item.added_option.all())
        if self.item:
            self.gravy_option.set(self.item.gravy_option.all())
        super().save(*args, **kwargs)
   
    def __str__(self):
        return f'Item {self.id} - {self.item.name}'
 
class MenuOption(models.Model):
    category = models.CharField(max_length=50)
    item = models.ManyToManyField(FoodMenuItem)

    def __str__(self):
        return self.category

class DietaryOption(models.Model):
    type = models.CharField(max_length=50)
    item = models.ManyToManyField(FoodMenuItem)

    def __str__(self):
        return self.type
    
class FoodPhoto(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    food = models.ForeignKey(FoodMenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo of {self.name}"
    
class DrinkPhoto(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    drink = models.ForeignKey(DrinkMenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo of {self.name}"
    
class Events(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"Event: {self.name}"

class EventPhoto(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    food = models.ForeignKey(FoodMenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo of {self.name}"

