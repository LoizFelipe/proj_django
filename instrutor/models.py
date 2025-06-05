from django.db import models

# Create your models here.

class Instrutor(models.Model):
    id = models.AutoField(primary_key=True,
                              help_text='id do Instrutor')
    rg = models.CharField(max_length=15,
                                 help_text='Informe o rg do Instrutor')
    nome = models.CharField(max_length=70,
                                 help_text='Informe o nome do Instrutor')
    dataNascimento = models.DateField(help_text='Informe a data de nascimento do Instrutor')
    telefone = models.CharField(max_length=9,
                                 help_text='Inform telefone do inst')
    ddd = models.CharField(max_length=3,
                                 help_text='Informe ddd')
    
    def __str__(self):
        return f'{self.id} - {self.rg}'

