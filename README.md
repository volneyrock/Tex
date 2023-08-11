# Sistema de Cadastro de Pessoas e CEP

Este projeto implementa uma API REST para o gerenciamento de um cadastro de pessoas. A API permite inserir, atualizar, excluir e ler os dados de pessoas, que consistem apenas nos campos "Nome" e "Idade", mas podem ser estendidos com campos adicionais, se necessário.
Também há um endpoint para COnsulta de CEP, que retorna os dados de endereço de um CEP informado e salva em um banco MongoDB local.

## Pré-requisitos

- Docker
- Docker Compose

## Como Executar a Aplicação

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   cd seuprojeto
   ```

2. **Inicie a Aplicação com o Docker Compose**:

   ```bash
   docker-compose up -d --build
   ```

   Isso iniciará os containers para a aplicação e o banco de dados MongoDB.

3. **Acesse a Aplicação**:

   A API estará disponível no endereço `http://localhost:8000/api`.

   Você pode usar o Postman para fazer as requisições ou acessar direto pela interface do Django Rest Framework, que estará disponível no endereço `http://localhost:8000/api/pessoa` por exemplo.

## Endpoints da API

- **Consultar CEP**:
  - **URL**: `/api/cep/<cep>/`
  - **Método**: `GET`

- **Inserir uma Nova Pessoa**:
  - **URL**: `/api/pessoa/`
  - **Método**: `POST`
  - **Body**: `{'nome': 'Nome da Pessoa', 'idade': 30}`

- **Atualizar os Dados de uma Pessoa**:
  - **URL**: `/api/pessoa/<id>/`
  - **Método**: `PUT`
  - **Body**: `{'nome': 'Novo Nome', 'idade': 31}`

- **Excluir uma Pessoa**:
  - **URL**: `/api/pessoa/<id>/`
  - **Método**: `DELETE`

- **Ler os Dados de Todas as Pessoas Cadastradas**:
  - **URL**: `/api/pessoa/`
  - **Método**: `GET`

- **Ler os Dados de uma Pessoa Específica**:
    - **URL**: `/api/pessoa/<id>/`
    - **Método**: `GET`

## Verificar dados no MongoDB

Você pode verificar os dados salvos no MongoDB usando o Mongo compass conectando no endereço `mongodb://localhost:27017` e acessando o banco `tex_db` e a coleção `pessoas` ou `endereco` .