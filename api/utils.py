import re
from bson.errors import InvalidId


def validar_object_id(object_id):
    if not re.match(r'^[a-f0-9]{24}$', object_id):
        raise InvalidId(f"'{object_id}' não é um ObjectID válido.")
