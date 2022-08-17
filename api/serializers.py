# serializar informação, nada mais é que pegar ela do sistema e transforma-la em json e retornar pra quem ta consumindo a API

from rest_framework import serializers
from pessoa.models import Contato, Pessoa


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone']


class PessoaSerializer(serializers.ModelSerializer):
    contatos = ContatoSerializer(many=True, read_only=True)

    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'ativa', 'contatos']