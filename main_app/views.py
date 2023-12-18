import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .models import FoodMenuItem, FoodPhoto, DrinkMenuItem

def home(request):
    return render(request, 'home.html')

class FoodMenuItemList(ListView):
    model = FoodMenuItem

class FoodMenuItemDetail(DetailView):
    model = FoodMenuItem

class FoodMenuItemCreate(CreateView):
    model = FoodMenuItem
    fields = '__all__'

class FoodMenuItemUpdate(UpdateView):
    model = FoodMenuItem
    fields = '__all__'

class FoodMenuItemDelete(DeleteView):
    model = FoodMenuItem
    success_url = '/menu/food'

class DrinkMenuItemList(ListView):
    model = DrinkMenuItem

class DrinkMenuItemDetail(DetailView):
    model = DrinkMenuItem

class DrinkMenuItemCreate(CreateView):
    model = DrinkMenuItem
    fields = '__all__'

class DrinkMenuItemUpdate(UpdateView):
    model = DrinkMenuItem
    fields = '__all__'

class DrinkMenuItemDelete(DeleteView):
    model = DrinkMenuItem
    success_url = '/menu/drinks'

def add_photo(request, foodmenuitem_id):
    foodmenuitem = FoodMenuItem.objects.get(pk=foodmenuitem_id)
    existing_photo = FoodPhoto.objects.filter(food=foodmenuitem).exists()
    if existing_photo:
        FoodPhoto.objects.filter(food=foodmenuitem).delete()
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = foodmenuitem.name + '_' + str(foodmenuitem_id) + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            FoodPhoto.objects.create(url=url, food=foodmenuitem, name=foodmenuitem)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('food_menu_item_detail', pk=foodmenuitem_id)