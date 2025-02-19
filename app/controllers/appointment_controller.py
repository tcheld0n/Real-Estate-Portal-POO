from app.data.database import db
from app.models.appointment import Appointment
from app.models.client import Client
from app.models.agent import Agent

class AppointmentController:
    def schedule_appointment(self, id, client_id, agent_id, property_id, date_time):
        client = self.find_client_by_id(client_id)
        agent = self.find_agent_by_id(agent_id)
        if client and agent:
            new_appointment = Appointment(id, client, agent, property_id, date_time)
            db.add_appointment(new_appointment)
            return new_appointment
        return None

    def list_appointments(self):
        return [vars(appt) for appt in db.appointments]

    def find_appointment_by_id(self, appointment_id):
        for appt in db.appointments:
            if appt.id == appointment_id:
                return appt
        return None

    def cancel_appointment(self, appointment_id):
        appointment_to_cancel = self.find_appointment_by_id(appointment_id)
        if appointment_to_cancel:
            db.appointments.remove(appointment_to_cancel)
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
