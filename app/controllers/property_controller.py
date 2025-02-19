from app.data.database import db
from app.models.property import Property
from app.models.agent import Agent

class PropertyController:
    def add_property(self, id, title, description, price, location, agent: Agent):
        new_property = Property(id, title, description, price, location, agent)
        db.add_property(new_property)
        agent.add_property(new_property)
        return new_property

    def list_properties(self):
        return [vars(prop) for prop in db.properties]

    def find_property_by_id(self, property_id):
        for prop in db.properties:
            if prop.id == property_id:
                return prop
        return None

    def update_property(self, property_id, title=None, description=None, price=None, location=None):
        property_to_update = self.find_property_by_id(property_id)
        if property_to_update:
            property_to_update.update_details(title, description, price, location)
            return property_to_update
        return None

    def delete_property(self, property_id):
        property_to_delete = self.find_property_by_id(property_id)
        if property_to_delete:
            db.properties.remove(property_to_delete)
            return True
        return False
