from django.urls import path
from .views import EventUpdate, HomeView, EventCreate, EventDelete, register, login

'''
from django.http import HttpResponse

def my_view(request):
    return HttpResponse(" Alguma coisa")
'''

urlpatterns = [
    #(caminho, view.py )
    #path('sobre/', my_view),
    path('', HomeView.as_view(), name = 'home'),
    path('criar-evento/', EventCreate.as_view(), name = 'criar-evento'),
    path('atualizar-evento/<int:pk>/', EventUpdate.as_view(), name= 'atualizar-evento'),
    path('<int:pk>/delete/', EventDelete.as_view(), name= 'deletar-evento' ),
    
    #autenticação
    path('cadastro/', register, name = 'cadastro'),
    path('login/', login, name = 'login'),
]



