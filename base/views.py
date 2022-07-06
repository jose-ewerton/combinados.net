#from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
'''
context = {
    'name' = 'Ewerton',
}

def home(request):
    return render('home.html')
'''
class HomeView(TemplateView):
    template_name = 'home.html'
