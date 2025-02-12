class Usuario():    
    # Inicializador com atributos de instância 
    def __init__(self, nome, email, senha, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo #comprador, locatario, agente, admin

    # Métodos
    # def cadastrar_usuario(self):
    #     self.nome  = input("Insira seu nome: ")
    #     self.email = input("Insira seu e-mail: ")
    #     self.senha = input("Insira sua senha: ")
    #     return f"Usuário {self.nome} cadastrado com sucesso!"
    # codigo comentado, aparentemente, desnecessário devido ao metodo __init__ usado em python

    def editar_perfil(self, novo_nome, novo_email, nova_senha):
        self.nome = novo_nome
        self.emai = novo_email
        self.senha = nova_senha
        
        return "Perfil atualizado com sucesso!"
    
class Propriedade():
    def __init__(self, id, proprietario, area, preco, localizacao, tipo, status):
        self.id = id
        self.proprietario = proprietario
        self.area = area
        self.preco = preco
        self.localizacao = localizacao
        self.tipo = tipo
        self.status = status

    def alterar_status(self, id, novo_status):
        self.id = id
        self.status = novo_status
        return f"Status da propriedade {id} atualizado para {novo_status}"
    
    def exibir_detalhes(self):
        return f"ID: {self.id}/nProprietário: {self.proprietario}/nÁrea (metros^2): {self.area}/nPreço: {self.preco}/nLocalização: {self.localizacao}/nTipo: {self.tipo}/nStatus: {self.status}"

class Visita():
    def __init__(self, id, usuario, propriedade, data):
        self.id = id #id da visita
        self.usuario = usuario #reponsavel pelo agendamento
        self.propriedade = propriedade
        self.data = data

    def exibir_detalhes(self):
        return f"Visita ID: {self.id}/nUsuário: {self.usuario.nome}/nPropriedade ID: {self.propriedade.id}, Data: {self.data}"
        
# Avaliação

# - id (identificador do usuario avaliador)
# - propriedade
# - nota
class Avaliacao():
    def __init__(self, id, propriedade, nota):
        self.id = id #Aqui seria melhor id ou usuario
        self.propriedade = propriedade
        self.nota = nota

    # def fazer_avaliacao(self):

    # def exibirr_avaliacao(self):
    
# Financiamento

# - Atributos:
#     - id
#     - preco
#     - parcelas
#     - taxa
# - Métodos:
#     - simular_financiamento

class Financiamento:
    def __init__(self, id, preco, parcelas, taxa):
        self.id = id
        self.preco = preco
        self.parcelas = parcelas
        self.taxa = taxa
    
    # def exibir_financiamento(self):