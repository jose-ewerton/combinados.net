from asyncio import events
from multiprocessing import Event
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Event
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.


#paginas do site
class HomeView(TemplateView):
    template_name = 'core/pages/home.html'

#CRUD for event

class EventCreate(CreateView):
    model = Event
    fields = ['title', 'event_type', 'description']
    template_name = 'core/pages/forms.html'
    success_url = reverse_lazy('home')