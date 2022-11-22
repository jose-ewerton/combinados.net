from django.urls import path
from . import views

urlpatterns = [
    
    #autenticação
    path('cadastro/', views.register, name = 'cadastro'),
    path('login/', views.login, name = 'login'),
    path('', views.HomeView.as_view(), name = 'home'),
    
    #CRUD para criar combinados
    path('criar-combinado/', views.CombinationCreate.as_view(), name = 'criar-combinado'),
    path('atualizar-combinado/<int:pk>/', views.CombinationUpdate.as_view(), name= 'atualizar-combinado'),
    path('listar-combinados/', views.CombinationList.as_view(), name = 'listar-combinados'),
    path('<int:pk>/deletar-combinado/', views.CombinationDelete.as_view(), name= 'deletar-combinado' ),
    
    #páginas logado
    path('home2/', views.Home2View.as_view(), name = 'home2'),
    #path('perfil/', Profile, name = 'perfil'),
]



