from pymongo import MongoClient


class EnderecoRepository:
    def __init__(self):
        client = MongoClient('mongo', 27017)
        self.collection = client['cep_database']['enderecos']
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
