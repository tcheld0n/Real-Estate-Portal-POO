class Property:
    def __init__(self, id, title, description, price, location, property_type, agent):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.location = location
        self.property_type = property_type     #sale, rent
        self.agent = agent
        self.available = True

    def update_details(self, title=None, description=None, price=None, location=None, property_type=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if price:
            self.price = price
        if type:
            self.property_type = property_type
        if location:
            self.location = location

    def switch_status(self):
        self.available = False