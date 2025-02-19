from app.models.user import User

class Agent(User):
    def __init__(self, id, name, email, agency):
        super().__init__(id, name, email)
        self.agency = agency
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)