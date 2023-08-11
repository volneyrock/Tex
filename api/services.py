from pymongo import MongoClient
from api.models import Pessoa
from bson import ObjectId
from api.utils import validar_object_id
from bson.errors import InvalidId
from rest_framework.exceptions import ValidationError


class EnderecoRepository:
    def __init__(self):
        client = MongoClient('mongo', 27017)
        self.collection = client['tex_db']['enderecos']
        self.collection.create_index('CEP', unique=True)

    def salvar(self, endereco_data):
        self.collection.update_one(
            {'CEP': endereco_data['CEP']},
            {'$set': endereco_data},
            upsert=True
        )


class EnderecoService:
    def __init__(self, viacep_client, endereco_repository):
        self.viacep_client = viacep_client
        self.endereco_repository = endereco_repository

    def consulta_cep(self, cep):
        endereco_data = self.viacep_client.get_endereco(cep)

        if endereco_data:
            endereco = {
                "Bairro": endereco_data['bairro'],
                "Cidade": endereco_data['localidade'],
                "UF": endereco_data['uf'],
                "CEP": endereco_data['cep'],
                "Logradouro": endereco_data['logradouro'],
                "Complemento": endereco_data.get('complemento', "")
            }
            return endereco
        return None

    def salvar_endereco(self, endereco):
        self.endereco_repository.salvar(endereco)


class PessoaRepository:
    def __init__(self):
        client = MongoClient('mongo', 27017)
        self.collection = client['tex_db']['pessoas']

    def salvar(self, pessoa):
        document = {
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        result = self.collection.insert_one(document)
        pessoa._id = str(result.inserted_id)

    def atualizar(self, pessoa_id, pessoa_data):
        result = self.collection.update_one(
            {'_id': ObjectId(pessoa_id)},
            {'$set': pessoa_data}
        )
        return result.modified_count > 0

    def excluir(self, pessoa_id):
        self.collection.delete_one({'_id': ObjectId(pessoa_id)})

    def buscar_todos(self):
        return [Pessoa(**pessoa) for pessoa in self.collection.find({})]

    def buscar_por_id(self, pessoa_id):
        pessoa = self.collection.find_one({'_id': ObjectId(pessoa_id)})
        if pessoa:
            return Pessoa(**pessoa)
        return None
