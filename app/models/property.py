class Property:
    def __init__(self, id, title, description, price, location, agent, type):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.location = location
        self.agent = agent
        self.type = type     #sale, rent
        self.available = True

    def update_details(self, title=None, description=None, price=None, location=None, type=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if price:
            self.price = price
        if type:
            self.type = type
        if location:
            self.location = location

    def switch_status(self):
        self.available = False