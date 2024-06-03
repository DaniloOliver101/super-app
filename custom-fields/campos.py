# campos.py
from flask import Blueprint, request
from db_config import get_db

campos = Blueprint('campos', __name__)
collection = get_db('campos')

# Resto do código...

@campos.route('/config/campos', methods=['POST'])
def add_field():
    field_name = "custom-" + request.json['nomeCampo']
    field_type = request.json['tipoInformacao']
    collection.update_one({"id": "123"}, {"$set": {field_name: field_type}})
    return '', 204

@campos.route('/config/campos', methods=['GET'])
def list_fields():
    # Obter um documento específico
    doc = collection.find_one({"id": "123"})

    # Se o documento não existe, retornar um erro
    if doc is None:
        return 'Documento não encontrado', 404

    # Remover o campo _id, que é adicionado automaticamente pelo MongoDB
    del doc['_id']

    # Retornar as chaves do documento, que são os nomes dos campos
    return doc.keys(), 200