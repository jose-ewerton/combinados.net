from django.urls import path
from .views import HomeView

'''
from django.http import HttpResponse

def my_view(request):
    return HttpResponse(" Alguma coisa")
'''

urlpatterns = [
    #(caminho, view.py )
    #path('sobre/', my_view),
    path('', HomeView.as_view(), name = 'home'),
]