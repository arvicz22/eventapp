from django import forms
from django.forms import ModelForm
from .models import *

class EventForm(ModelForm):
    
    class Meta:
        model = Event
        fields = ['title','description','time','location','food_provided']