from app.data.database import db
from app.models.client import Client

class ClientController:
    def add_client(self, id, name, email, phone):
        new_client = Client(id, name, email, phone)
        db.add_client(new_client)
        return new_client

    def list_clients(self):
        return [vars(client) for client in db.clients]

    def find_client_by_id(self, client_id):
        for client in db.clients:
            if client.id == client_id:
                return client
        return None

    def delete_client(self, client_id):
        client_to_delete = self.find_client_by_id(client_id)
        if client_to_delete:
            db.clients.remove(client_to_delete)
            return True
        return False
