from tiposdeatividade.models import TiposDeAtividade
from titulo.models import Titulo
from aluno.models import Aluno
from instrutor.models import Instrutor
from turma.models import Turma

from django.db import connection
from datetime import date
import random

# gerar valor aleatorio 
def gerar_numero_aleatorio_faixa(inicio, fim):
    return random.randint(inicio, fim)

# gerar data aleatoria
def gerar_data_aleatoria(tipo_data):
    dia = gerar_numero_aleatorio_faixa(1, 28)
    mes = gerar_numero_aleatorio_faixa(1, 12)
    ano = 0

    if tipo_data =='inicial':
        ano = gerar_numero_aleatorio_faixa(1970, 2007)
    else:
        ano = gerar_numero_aleatorio_faixa(2021, 2024)

    return date(dia, mes, ano)        


# truncar tableas para zerar o contador de auto-incremento
def truncate_table(nome_tabela):
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM {nome_tabela}')
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name = "{nome_tabela}"')

def truncar_tabelas():
    truncate_table('turma_turma')
    truncate_table('instrutor_instrutor')
    truncate_table('aluno_aluno')
    truncate_table('titulo_titulo')
    truncate_table('tiposdeatividade_tiposdeatividade')

# popular tabela com tipos de atividade
def popular_aluno():
    lista_aluno = []

    for i in range(1,50):
        lista_aluno.append(
            Aluno(
                nome = 'Aluno' + f'{i:02}',
                dataInicial = gerar_data_aleatoria('incial'),
                dataFinal = gerar_data_aleatoria('inicial')
        ) 
    )
    Aluno.objects.bulk_create(lista_aluno)


def popular_tiposdeatividade():
    lista_tiposdeatividade = []

    for i in range(1,10):
        lista_tiposdeatividade.append(TiposDeAtividade(descricao='Atividade ' + f'{i:02}'))

    TiposDeAtividade.objects.bulk_create(lista_tiposdeatividade)


def popular_titulo():
    lista_titulo = []

    for i in range(1,10):
        lista_titulo.append(
            Titulo(
                codigo='Titulo' + f'{i:02}',
                descricao='Titulo' + f'{i:02}',))

    Titulo.objects.bulk_create(lista_titulo)


def popular_instrutor():
    lista_instrutor = []

    for i in range(1,11):
        lista_instrutor.append(
            Instrutor(
                nome = 'Instrutor' + f'{i:02}',
                data_nascimento = gerar_data_aleatoria('nascimento'),
                rg = 'RG' + f'{i:013}'
                )
        )

    Instrutor.objects.bulk_create(lista_instrutor)

def popular_turma():
    lista_turma = []

    for i in range(1,10):
        lista_turma.append(Turma(descricao='Atividade ' + f'{i:02}'))

    Turma.objects.bulk_create(lista_turma)