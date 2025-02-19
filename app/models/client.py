from app.models.user import User

class Client(User):
    def __init__(self, id, name, email, phone):
        super().__init__(id, name, email)
        self.phone = phone
        self.appointments = []

    def request_appointment(self, appointment):
        self.appointments.append(appointment)