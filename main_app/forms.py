from django import forms
from .models import LineItem, Order
from django.forms import EmailField 
from django.forms.models import inlineformset_factory
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=False, 
        help_text=_("Enter email to hear about upcoming events."))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
class LineItemForm(forms.ModelForm):
    class Meta:
        model = LineItem
        fields = '__all__'

class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("name", "pickup_deliver", "phone", "address")
