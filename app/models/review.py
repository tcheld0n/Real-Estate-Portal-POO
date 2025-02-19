from datetime import datetime

class Review:
    def __init__(self, id, property, user, rating, comment):
        self.id = id
        self.property = property
        self.user = user
        self.rating = rating
        self.comment = comment
        self.date = datetime.now()

    def update_review(self, rating=None, comment=None):
        if rating:
            self.rating = rating
        if comment:
            self.comment = comment