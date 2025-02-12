# Real-Estate-Portal-POO

Este é um sistema simples para gerenciamento de imóveis, permitindo cadastro de usuários, propriedades, agentes imobiliários e agendamento de visitas. O sistema está sendo desenvolvido sob o paradigma orientado à objetos.

### Classes:

Usuario

- Atributos
    - nome
    - email
    - senha
    - tipo: comprador, locatario, agente, admin
- Métodos:
    - cadastrar_usuario()
    - editar_perfil(novo_nome, novo_email, nova_senha)

Propriedade

- Atributos
    - id: identificador da propriedade
    - proprietario
    - area: em m^2
    - preco
    - localizacao: cidade
    - tipo: casa, apartamento, terreno, etc
    - status: disponível, vendido, alugado
- Métodos:
    - alterar_status(novo_status)
    - exibir_detalhes()

Visita 

- id (identificador da visita)
- usuario (responsável pelo agendamento)
- propriedade
- data

Avaliação

- id (identificador do usuario avaliador)
- propriedade
- nota

Financiamento

- Atributos:
    - id
    - preco
    - parcelas
    - taxa
- Métodos:
    - simular_financiamento