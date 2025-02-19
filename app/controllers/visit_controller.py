from app.data.database import db

class VisitController:
    def schedule_visit(self, id, client_id, agent_id, property_id, date_time):
        client = self.find_client_by_id(client_id)
        agent = self.find_agent_by_id(agent_id)
        if client and agent:
            new_visit = visit(id, client, agent, property_id, date_time)
            db.add_visit(new_visit)
            return new_visit
        return None

    def list_visits(self):
        return [vars(visit) for visit in db.visits]

    def find_visit_by_id(self, visit_id):
        for visit in db.visits:
            if visit.id == visit_id:
                return visit
        return None

    def cancel_visit(self, visit_id):
        visit_to_cancel = self.find_visit_by_id(visit_id)
        if visit_to_cancel:
            db.visits.remove(visit_to_cancel)
            return True
        return False

    def find_client_by_id(self, client_id):
        for client in db.clients:
            if client.id == client_id:
                return client
        return None

    def find_agent_by_id(self, agent_id):
        for agent in db.agents:
            if agent.id == agent_id:
                return agent
        return None
