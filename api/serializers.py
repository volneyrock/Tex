from rest_framework import serializers


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
