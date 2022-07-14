from django.forms import fields, models, ModelForm
from .models import Pessoa


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'ativa']