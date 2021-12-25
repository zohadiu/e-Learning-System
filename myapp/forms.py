from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from.models import Order

# class ModelForm(ModelForm):
    
#     class Meta:
#         model = Order
#         fields = '__all__'
class CreaterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
