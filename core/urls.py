from django.urls import path
from .views import HomeView, Home2View, CombinationCreate, CombinationUpdate, CombinationDelete, Profile, register, login

'''
from django.http import HttpResponse

def my_view(request):
    return HttpResponse(" Alguma coisa")
'''

urlpatterns = [
    #(caminho, view.py )
    #path('sobre/', my_view),
    path('', HomeView.as_view(), name = 'home'),
    path('criar-combinado/', CombinationCreate.as_view(), name = 'criar-combinado'),
    path('atualizar-combinado/<int:pk>/', CombinationUpdate.as_view(), name= 'atualizar-combinado'),
    path('<int:pk>/deletar-combinado/', CombinationDelete.as_view(), name= 'deletar-combinado' ),
    
    #autenticação
    path('cadastro/', register, name = 'cadastro'),
    path('login/', login, name = 'login'),
    
    #páginas logado
    path('home2/', Home2View, name = 'home2'),
    path('perfil/', Profile, name = 'perfil'),
]



