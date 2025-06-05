from django.db import models

# Create your models here.

class Turma(models.Model):
    numero = models.AutoField(primary_key=True,
                              help_text='numero da Turma')
    horarioAula = models.TimeField( help_text='Informe horarioAula da aula')
    duracoaAula = models.SmallIntegerField( help_text='Informe duração')
    dataInicial = models.DateField(help_text='Informe data inicial')
    dataFinal = models.DateField(help_text='Informe data final')
    
    def __str__(self):
        return f'{self.numero} - {self.horarioAula}'

