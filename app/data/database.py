# Simulação de Banco de Dados em Memória
from app.models.property import Property
from app.models.agent import Agent
from app.models.client import Client
from app.models.appointment import Appointment
from app.models.review import Review

class Database:
    def __init__(self):
        self.properties = []  # Lista de imóveis
        self.agents = []      # Lista de agentes
        self.clients = []     # Lista de clientes
        self.appointments = []  # Lista de agendamentos de visitas
        self.reviews = []      # Lista de avaliações

    def add_property(self, property: Property):
        self.properties.append(property)

    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    def add_client(self, client: Client):
        self.clients.append(client)

    def add_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)

    def add_review(self, review: Review):
        self.reviews.append(review)

# Instância global do banco de dados para ser usada em todo o sistema
db = Database()