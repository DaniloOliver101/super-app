import requests
import json
import time

BASE_URL = 'http://localhost:5000/clientes'  # substitua pelo URL da sua API

def post_cliente():
    response = requests.post(BASE_URL, json={'id': '1', 'nome': 'Teste', 'cpf': '12345678901', 'email': 'teste@teste.com', 'status': 'ativo'})
    print('Cliente criado', response.status_code)
    time.sleep(2)

def get_clientes():
    response = requests.get(BASE_URL)
    data = response.json()
    print('Cliente listado', data)
    time.sleep(2)

def get_cliente_by_cpf(cpf):
    response = requests.get(f'{BASE_URL}/cpf/{cpf}')
    data = response.json()
    if response.status_code == 200:
        print('Cliente encontrado', data)
    else:
        print('Cliente não encontrado', response.status_code)
    time.sleep(2)

def put_cliente():
    response = requests.put(f'{BASE_URL}/cpf/12345678901', json={'nome': 'Teste Alterado'})
    print('Cliente atualizado', response.status_code)
    time.sleep(2)

def patch_cliente():
    response = requests.patch(f'{BASE_URL}/cpf/12345678901/status', json={'status': 'inativo'})
    print('Status do cliente atualizado', response.status_code)
    time.sleep(2)

def delete_clientes():
    response = requests.delete(BASE_URL)
    print('Clientes deletados', response.status_code)
    time.sleep(2)

def delete_cliente():
    response = requests.delete(f'{BASE_URL}/cpf/12345678901')
    print('Cliente deletado', response.status_code)
    time.sleep(2)

def run_tests():
    delete_clientes()
    post_cliente()
    #get_clientes()
    get_cliente_by_cpf('12345678901')
    put_cliente()
    get_cliente_by_cpf('12345678901')
    #patch_cliente()
    get_cliente_by_cpf('12345678901')
    delete_cliente()
    #get_clientes()

if __name__ == '__main__':
    run_tests()