from django import forms

# classe formulario para inclusao
class TituloForm(forms.Form):
    descricao = forms.CharField(max_length=100,
                                required=True,
                                help_text='informe a descrição do Titulo')