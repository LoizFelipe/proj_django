from django.db import models

# Create your models here.

class Titulo(models.Model):
    codigo = models.AutoField(primary_key=True,
                              help_text='código do Titulo')
    descricao = models.CharField(max_length=70,
                                 help_text='Informe a descrição do Titulo')
    
    def __str__(self):
        return f'{self.codigo} - {self.descricao}'
