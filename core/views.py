from http.client import HTTPResponse
from django.views.generic import TemplateView
from .models import Event
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

# Create your views here.


#paginas do site
class HomeView(TemplateView):
    template_name = 'core/pages/home.html'

@login_required    
class PersonalView(TemplateView):
    template_name = 'core/pages/personal.html'

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
    

def register(request):
    if request.method == 'GET':
        return render(request, "core/pages/register.html")
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username).first()   
        if user:
            return render(request, "core/pages/permission.html")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return render(request, "core/pages/home.html")

def login(request):
    if request.method == 'GET':
        return render(request, "core/pages/login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login_django(request, user)
            return render(request, "core/pages/personal.html") 
            
        else:
           return render(request, "core/pages/register.html") 
