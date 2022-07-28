import re
from django.forms import fields, models, ModelForm, DateField, TextInput
from .models import Contato, Pessoa


class PessoaForm(ModelForm):
    data_nascimento = DateField(
        widget=TextInput(
            attrs = {"type": "date"}
        )
    , required=True)
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'ativa']

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone']