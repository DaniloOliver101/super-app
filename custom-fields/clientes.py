from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from db_config import get_db

clientes = Blueprint('clientes', __name__)
collection = get_db('clientes')

# ... código existente ...
@clientes.route('/clientes', methods=['DELETE'])
def delete_all_clientes():
    collection.delete_many({})
    return '', 204

@clientes.route('/clientes/cpf/<cpf>', methods=['GET'])
def get_cliente_by_cpf(cpf):
    cliente = collection.find_one({'cpf': cpf})
    if cliente:
        cliente['_id'] = str(cliente['_id'])
        return jsonify(cliente), 200
    else:
        return jsonify({'error': 'Cliente não encontrado'}), 404

@clientes.route('/clientes/cpf/<cpf>', methods=['DELETE'])
def delete_cliente(cpf):
    result = collection.delete_one({'cpf': cpf})
    if result.deleted_count > 0:
        return '', 204
    else:
        return jsonify({'error': 'Cliente não encontrado'}), 404

@clientes.route('/clientes/cpf/<cpf>', methods=['PUT'])
def update_cliente(cpf):
    cliente = request.json
    result = collection.update_one({'cpf': cpf}, {'$set': cliente})
    if result.modified_count > 0:
        return '', 204
    else:
        return jsonify({'error': 'Cliente não encontrado'}), 404

@clientes.route('/clientes/cpf/<cpf>/status', methods=['PATCH'])
def update_status_cliente(cpf):
    status = request.json.get('status', '')
    result = collection.update_one({'cpf': cpf}, {'$set': {'status': status}})
    if result.modified_count > 0:
        return '', 204
    else:
        return jsonify({'error': 'Cliente não encontrado'}), 404


@clientes.route('/clientes', methods=['POST'])
def add_cliente():
    cliente = request.json
    required_fields = ['id', 'nome', 'cpf', 'email', 'status']

    if not all(field in cliente for field in required_fields):
        return jsonify({'error': 'Faltando campo obrigatório'}), 400

    result = collection.insert_one(cliente)
    cliente['_id'] = str(result.inserted_id)
    return jsonify(cliente), 201

@clientes.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = list(collection.find())
    for cliente in clientes:
        cliente['_id'] = str(cliente['_id'])
    return jsonify(clientes), 200