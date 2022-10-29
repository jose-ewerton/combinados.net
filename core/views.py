from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect

from .models import Combined

# Create your views here.


#pagina principal do site
class HomeView(TemplateView):
    template_name = 'core/pages/home.html'


#CRUD for event

class CombinationCreate(CreateView):
    model = Combined
    fields = ['combination_title', 'combination_category', 'combination_description']
    template_name = 'core/pages/forms.html'
    success_url = reverse_lazy('home')
    
class CombinationUpdate(UpdateView):
    model = Combined
    fields = ['combination_title', 'combination_category', 'combination_description']
    template_name = 'core/pages/forms.html'
    success_url = reverse_lazy('home')

class CombinationList(UpdateView):
    model = Combined
    fields = ['combination_title', 'combination_category', 'combination_description']
    template_name = 'core/pages/forms.html'
    success_url = reverse_lazy('home')

class CombinationDelete(DeleteView):
    model = Combined
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
            return redirect('home2')         
        else:
            return HttpResponseRedirect(reverse('cadastro')) 



#página principal logado no site  

@login_required  
class Home2View(TemplateView):
    template_name = 'core/pages/home2.html'

#@login_required 
#class Profile(TemplateView):
#    template_name = 'core/pages/profile.html'  

