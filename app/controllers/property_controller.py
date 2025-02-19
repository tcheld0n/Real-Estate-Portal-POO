from app.data.database import db
from app.models.property import Property
from app.models.user import User

class PropertyController:
    def add_property(self, id, title, description, price, location, property_type, user: User):
        new_property = Property(id, title, description, price, location, property_type, user)
        db.add_property(new_property)        # Adiciona ao banco de dados
        user.add_property(new_property)      # Associa ao usuário (agente)
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
    def search_property_by_type(self, property_type):
        return [prop for prop in db.get_properties() if prop.property_type.lower() == property_type.lower()]

    def search_property_by_location(self, location):
        return [prop for prop in db.get_properties() if location.lower() in prop.location.lower()]

    def search_property_by_price_range(self, price_min, price_max):
        return [prop for prop in db.get_properties() if price_min <= prop.price <= price_max]
