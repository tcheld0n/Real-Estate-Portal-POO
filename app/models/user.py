class User:
    def __init__(self, user_id, name, email, password, user_type):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.user_type = user_type  # Cliente ou Agente

        # Apenas agentes possuem uma lista de propriedades
        if self.user_type == "Agente":
            self.properties = []
        else:
            self.properties = None

    # Adiciona a propriedade a lista do agente
    def add_property(self, property):
        if self.user_type != "Agente":
            raise Exception("Erro: Apenas agentes podem adicionar propriedades!")
        self.properties.append(property)

    def list_properties(self):
        if self.user_type != "Agente":
            raise Exception("Erro: Somente agentes possuem propriedades!")
        return self.properties

    def __str__(self):
        return f"{self.user_type} - {self.name} ({self.email})"