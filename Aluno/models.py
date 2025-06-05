from django.db import models

# Create your models here.

class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True,
                              help_text='matricula do Aluno')
    nome = models.CharField(max_length=70,
                                 help_text='Informe nome do Aluno')
    dataInicial = models.DateTimeField(help_text='Informe a data inicial')
    dataFinal = models.DateTimeField(help_text='Informe a data final')
    
    
    def __str__(self):
        return f'{self.matricula} - {self.nome}'



