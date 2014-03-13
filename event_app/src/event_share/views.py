#python first
# from pymongo import Connection

#djangp second
from django import forms
from django.forms import ModelForm
from .models import *
from .forms import *

#apps
from django.conf import settings
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.core.mail import send_mail

#utils
# connection = Connection()

# MY VIEWS

def home(request):
    
    event_list = Event.objects.all()
    return render_to_response("home.html",
                                locals(),
                                context_instance=RequestContext(request))

def create(request):
    form = EventForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            save_it = form.save()
            save_it.save()
            messages.success(request, "Thanks for your feedback!")
        else:
            messages.success(request, "Form is invalid!")
    
    return render_to_response("create.html",
                                locals(),
                                context_instance=RequestContext(request))
    
def display_events(request):
    
    # gather all of the events
    # list them as event_list
    

    return render_to_response("display_events.html",
                                locals(),
                                context_instance=RequestContext(request))