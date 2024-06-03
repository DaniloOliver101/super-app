Funcionalidade: Cadastro de Clientes Dinâmico
  Como um usuário da API
  Quero ser capaz de cadastrar clientes com campos dinâmicos
  Para que eu possa personalizar as informações que colecionei para cada cliente

  Cenário: Cadastrando um novo cliente
    Dado que eu tenho um novo cliente para cadastrar
    Quando eu envio uma requisição POST para "/clientes" com o nome, CPF e email do cliente
    Então o cliente é cadastrado com sucesso

  Cenário: Adicionando um novo campo ao cadastro do cliente
    Dado que eu quero adicionar um novo campo ao cadastro do cliente
    Quando eu envio uma requisição POST para "/clientes/campos" com o nome do campo e o tipo de dado
    Então o novo campo é adicionado com sucesso ao cadastro do cliente

  Cenário: Cadastrando um cliente com o novo campo
    Dado que eu tenho um novo cliente para cadastrar
    E eu adicionei um novo campo ao cadastro do cliente
    Quando eu envio uma requisição POST para "/clientes" com o nome, CPF, email e o novo campo do cliente
    Então o cliente é cadastrado com sucesso