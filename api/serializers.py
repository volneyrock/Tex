from rest_framework import serializers
from api.models import Pessoa
from api.services import PessoaRepository
from api.utils import validar_object_id
from bson.errors import InvalidId


class EnderecoSerializer(serializers.Serializer):
    cep = serializers.CharField(source='CEP')
    logr = serializers.CharField(source='Logradouro')
    compl = serializers.CharField(source='Complemento')
    bairro = serializers.CharField(source='Bairro')
    cidade = serializers.CharField(source='Cidade')
    uf = serializers.CharField(source='UF')


class RespostaCEPSerializer(serializers.Serializer):
    sucesso = serializers.BooleanField()
    endereco = EnderecoSerializer()


class PessoaSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    nome = serializers.CharField(required=True)
    idade = serializers.IntegerField(required=True)

    def create(self, validated_data):
        pessoa = Pessoa(None, validated_data['nome'], validated_data['idade'])
        repository = PessoaRepository()
        repository.salvar(pessoa)
        return pessoa

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.idade = validated_data.get('idade', instance.idade)
        repository = PessoaRepository()
        repository.atualizar(str(instance._id), validated_data)
        return instance
