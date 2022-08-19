from django.db import models

# Create your models here.


class Base(models.Model):
    creation = models.DateField("Data de criação", auto_now_add=True)
    modified = models.DateField("Data de atualização", auto_now= True)
    active = models.BooleanField("Ativo?", default= True)
    
    class Meta:
        abstract = True

class User(Base):
    email = models.EmailField("E-mail", max_length=100)
    password = models.CharField("Senha", max_length=20)
    
    def __str__(self):
        return self.email
       
TYPES_EVENTS = (
    ('1', 'ATIVIDADES'),
    ('2', 'DOAÇÕES'),
)   
class Event(Base):
    title = models.CharField("Título do Evento", max_length=100)
    event_type = models.CharField("Tipo de evento", max_length=100, choices= TYPES_EVENTS)
    description = models.TextField("Descrição")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    
    def __str__(self):
        return self.title
    
class Task(Base):
    description = models.TextField("Descrição da tarefa")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
    
    
