from django.db import models
from django.utils import timezone

# Create your models here.

class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True,
                              help_text='matricula do Aluno')
    nome = models.CharField(max_length=70,
                                 help_text='Informe nome do Aluno')
    dataInicial = models.DateField(null = False,
                                   default =timezone.now(),
                                   help_text='Informe a data inicial')
    dataFinal = models.DateField(null = False,
                                 blank=True,
                                   default =timezone.now(),
                                   help_text='Informe a data final')
    
    
    def __str__(self):
        return f'{self.matricula} - {self.nome}'
    

    



