import requests


class ViaCEPClient:
    def __init__(self):
        self.base_url = 'https://viacep.com.br/ws/'

    def get_endereco(self, cep):
        url = self.base_url + cep + '/json/'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
