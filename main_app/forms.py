from django import forms
from .models import LineItem, Order, Profile
from django.forms import EmailField 
from django.forms.models import inlineformset_factory
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("phone", "street_address", "suburb", "postcode")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['street_address'].required = False
    def clean(self):
        cleaned_data = super().clean()
        pickup_deliver = cleaned_data.get('pickup_deliver')

        if pickup_deliver == 'P':
            self.fields['street_address'].required = False
        elif pickup_deliver == 'D':
            self.fields['street_address'].required = True

        return cleaned_data
    
class LineItemForm(forms.ModelForm):
    class Meta:
        model = LineItem
        fields = (
            "name", 
            "price", 
            "order", 
            "side_option",
            "added_option",
            "size_option",
            "gravy_option",
            "cook_option",
            "sauce_option",
            "remove_option"
        )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("name", "pickup_deliver")



