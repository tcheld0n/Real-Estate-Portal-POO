from app.data.database import db
from app.models.agent import Agent
from app.models.client import Client
from app.models.user import User

class UserController:
    def add_agent(self, id, name, email, agency):
        new_agent = Agent(id, name, email, agency)
        db.add_agent(new_agent)
        return new_agent

    def add_client(self, id, name, email, phone):
        new_client = Client(id, name, email, phone)
        db.add_client(new_client)
        return new_client

    def list_agents(self):
        return [vars(agent) for agent in db.agents]

    def list_clients(self):
        return [vars(client) for client in db.clients]

    def find_agent_by_id(self, agent_id):
        for agent in db.agents:
            if agent.id == agent_id:
                return agent
        return None

    def find_client_by_id(self, client_id):
        for client in db.clients:
            if client.id == client_id:
                return client
        return None

    def delete_agent(self, agent_id):
        agent_to_delete = self.find_agent_by_id(agent_id)
        if agent_to_delete:
            db.agents.remove(agent_to_delete)
            return True
        return False

    def delete_client(self, client_id):
        client_to_delete = self.find_client_by_id(client_id)
        if client_to_delete:
            db.clients.remove(client_to_delete)
            return True
        return False

    def authenticate_user(self, email, password):
        for user in db.users:
            if user.email == email and user.password == password:
                return user
        return None

    def register_user(self, name, email, password, user_type):
        new_user = User(len(db.users) + 1, name, email, password, user_type)
        db.users.append(new_user)
        print(f"Usuário {name} registrado com successo!")
        return new_user

    def update_user_profile(self, user_id, new_data):
        user = self.find_user_by_id(user_id)
        if user:
            for key, value in new_data.items():
                setattr(user, key, value)
            return True
        return False

    def find_user_by_id(self, user_id):
        for user in db.users:
            if user.id == user_id:
                return user
        return None