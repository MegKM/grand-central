import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .models import FoodMenuItem, FoodPhoto, DrinkMenuItem, Order, Event, EventPhoto
from .forms import UserCreationForm, ProfileForm
from .forms import LineItemForm, OrderForm

def home(request):
    event_list = Event.objects.all()
    context = {
        'event_list': event_list,

        }
    return render(request, 'home.html', context)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form = user_form.save()
            login(request, user_form)
            return redirect('home')
        else:
            if 'username' in user_form.errors:
                username_errors = user_form.errors['username']
                if 'This field may only contain letters, numbers, and @/./+/-/_ characters.' in username_errors:
                    error_message = 'Invalid characters in username. Please use only letters, numbers, and @/./+/-/_ characters.'
                elif 'A user with that username already exists.' in username_errors:
                    error_message = 'Username is already taken. Please choose a different one.'
                else:
                    error_message = 'Invalid username. Please choose a different one.'
            if 'password1' in user_form.errors or 'password2' in user_form.errors:
                error_message = 'Invalid password - passwords do not match or are weak.'
            else:
                error_message = 'Invalid sign up - try again'
    user_form = UserCreationForm()
    context = {
        'user_form': user_form, 
        'error_message': error_message}
    return render(request, 'registration/signup.html', context)

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

class EventCreate(CreateView):
    model = Event
    fields = '__all__'

class DrinkMenuItemDelete(DeleteView):
    model = DrinkMenuItem
    success_url = '/menu/drinks'

def add_food_photo(request, foodmenuitem_id):
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

def create_line_item(request, pk):
    foodmenuitem = FoodMenuItem.objects.get(pk=pk)
    error_message = ''  
    order = Order.objects.get(user=request.user, isInProgress=True)

    if request.method == 'POST':
        form = LineItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_menu')
        else:
            error_message = 'Failed'

    form = LineItemForm()
    context = {
        'form': form, 
        'error_message': error_message,
        'foodmenuitem': foodmenuitem,
        'order': order
        }

    return render(
        request,
        'addlineitem.html',
        context,
    )

def create_order(request):
    existing_order = Order.objects.filter(user=request.user).first()

    if existing_order and existing_order.isInProgress:
        return redirect('order_view')
        
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if order_form.is_valid() and profile_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()
            profile_form.save()
            return redirect('food_menu')
    else:
        order_form = OrderForm()
        profile_form = ProfileForm(instance=request.user.profile)
    
    context = {
        'order_form': order_form,
        'profile_form': profile_form
    }
    return render(request, 'create_order.html', context)

class EventList(ListView):
    model = Event

class EventDetail(DetailView):
    model = Event


def view_order(request):
    order = Order.objects.get(user=request.user, isInProgress=True)

    context = {
        'order': order
    }
    return render(request, 'view_order.html', context)


def add_event_photo(request, event_id):
    event = Event.objects.get(pk=event_id)
    existing_photo = EventPhoto.objects.filter(event=event).exists()
    if existing_photo:
        EventPhoto.objects.filter(event=event).delete()
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = event.name + '_' + str(event_id) + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            EventPhoto.objects.create(url=url, event=event, name=event)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('event_detail', pk=event_id)