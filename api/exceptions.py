from rest_framework.exceptions import APIException
from rest_framework import status


class CEPNaoEncontradoException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    erro = True
    mensagem = "CEP não encontrado"
