from app.data.database import db
from app.models.agent import Agent

class AgentController:
    def add_agent(self, id, name, email, agency):
        new_agent = Agent(id, name, email, agency)
        db.add_agent(new_agent)
        return new_agent

    def list_agents(self):
        return [vars(agent) for agent in db.agents]

    def find_agent_by_id(self, agent_id):
        for agent in db.agents:
            if agent.id == agent_id:
                return agent
        return None

    def delete_agent(self, agent_id):
        agent_to_delete = self.find_agent_by_id(agent_id)
        if agent_to_delete:
            db.agents.remove(agent_to_delete)
            return True
        return False