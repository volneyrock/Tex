class Pessoa:
    def __init__(self, _id, nome, idade):
        self._id = _id
        self.nome = nome
        self.idade = idade

    @classmethod
    def from_mongo_document(cls, document):
        return cls(
            _id=document['_id'],
            nome=document['nome'],
            idade=document['idade']
        )
