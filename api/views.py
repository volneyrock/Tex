from api.exceptions import CEPNaoEncontradoException
from api.serializers import RespostaCEPSerializer
from api.serializers import PessoaSerializer
from api.services import EnderecoService
from api.services import EnderecoRepository
from api.services import PessoaRepository
from api.via_cep import ViaCEPClient
from api.utils import validar_object_id
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bson.errors import InvalidId
from rest_framework.exceptions import ValidationError


class ConsultaCEPView(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.endereco_service = EnderecoService(
            ViaCEPClient(), EnderecoRepository()
        )

    def get(self, request, *args, **kwargs):
        cep = kwargs.get('cep')
        endereco = self.endereco_service.consulta_cep(cep)

        if endereco:
            self.endereco_service.salvar_endereco(endereco)
            serializer = RespostaCEPSerializer({
                "sucesso": True,
                "endereco": endereco
            })
            return Response(serializer.data)

        raise CEPNaoEncontradoException()


class PessoaView(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = PessoaRepository()

    def validar_id(self, pk):
        try:
            validar_object_id(pk)
        except InvalidId as e:
            raise ValidationError(str(e))

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            self.validar_id(pk)
            pessoa = self.repository.buscar_por_id(pk)
            if pessoa is None:
                return Response(
                    {'error': 'Pessoa não encontrada'},
                    status=status.HTTP_404_NOT_FOUND
                )
            return Response(PessoaSerializer(pessoa).data)

        pessoas = self.repository.buscar_todos()
        return Response(PessoaSerializer(pessoas, many=True).data)

    def post(self, request, *args, **kwargs):
        serializer = PessoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pessoa = serializer.save()
        return Response(PessoaSerializer(pessoa).data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.validar_id(pk)
        pessoa = self.repository.buscar_por_id(pk)
        if pessoa is None:
            return Response({'error': 'Pessoa não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PessoaSerializer(pessoa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.validar_id(pk)
        pessoa = self.repository.buscar_por_id(pk)
        if pessoa is None:
            return Response({'error': 'Pessoa não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.repository.excluir(pessoa._id)
        return Response(status=status.HTTP_204_NO_CONTENT)
