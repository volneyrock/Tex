from api.exceptions import CEPNaoEncontradoException
from api.serializers import RespostaCEPSerializer
from api.services import EnderecoService
from api.services import EnderecoRepository
from api.via_cep import ViaCEPClient
from rest_framework.views import APIView
from rest_framework.response import Response


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
