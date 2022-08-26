from django.views.generic import TemplateView
from .models import Event
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    
class EventUpdate(UpdateView):
    model = Event
    fields = ['title', 'event_type', 'description']
    template_name = 'core/pages/forms.html'
    success_url = reverse_lazy('home')

class EventDelete(DeleteView):
    model = Event
    template_name = 'core/pages/event_confirm_delete.html'
    success_url = reverse_lazy('home')