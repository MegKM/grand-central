import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .models import FoodMenuItem, FoodPhoto

def home(request):
    return render(request, 'home.html')

class FoodMenuItemList(ListView):
    model = FoodMenuItem

class FoodMenuItemDetail(DetailView):
    model = FoodMenuItem

@user_passes_test(lambda u: u.is_superuser)
class FoodMenuItemCreate(CreateView):
    model = FoodMenuItem
    fields = '__all__'

    def form_valid(self, form):
        response = super().form_valid(form)
        food_id = self.object.id
        photo_file = self.request.FILES.get('photo-file', None)

        if photo_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                FoodPhoto.objects.create(url=url, food_id=food_id)
            except Exception as e:
                print('An error occurred uploading file to S3')
                print(e)
        return response