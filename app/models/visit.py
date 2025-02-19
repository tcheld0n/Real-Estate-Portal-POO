class Visit:
    def __init__(self, id, client, property, date_time):
        self.id = id
        self.client = client
        self.property = property
        self.date_time = date_time
        self.status = "Scheduled"

    def reschedule(self, new_date_time):
        self.date_time = new_date_time

    def cancel(self):
        self.status = "Cancelled"