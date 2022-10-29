from django.db import models
#from django.contrib.auth.models import User

# Create your models here.


class Base(models.Model):
    creation = models.DateField("Data de criação", auto_now_add=True)
    modified = models.DateField("Data de atualização", auto_now= True)
    active = models.BooleanField("Ativo?", default= True)
    
    class Meta:
        abstract = True
       
TYPES_EVENTS = (
    ('1', 'ATIVIDADES'),
    ('2', 'DOAÇÕES'),
)   
class Combined(Base):
    combination_title = models.CharField("Título do Combinado", max_length=100, null= True)
    combination_category = models.CharField("Categoria de evento", max_length=100, choices= TYPES_EVENTS, null= True)
    combination_description = models.TextField("Descrição do Combinado", null= True)
    
    def __str__(self):
        return self.combination_title
    
class Task(Base):
    task_description = models.TextField("Descrição da tarefa", null= True)
    combination = models.ForeignKey(Combined, on_delete=models.CASCADE, null= True)
    
    def __str__(self):
        return self.description


#Criando um perfil e adicionando campos ao meu usuário

''' 
class Profile(Base):
    #Campos Adicionais   
    username = models.CharField("username", max_length=100, null= True) #permitir ser nulos na criação
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.user.email  
        
'''
