from extensions import db


class Odeal(db.Model):
    __tablename__ = 'odeal'
    id = db.Column(db.String, primary_key=True)
    Marka = db.Column(db.String)

    def __init__(self, id, Marka):
        self.id = id
        self.Marka = Marka

    def __repr__(self):
        return f"<Odeal {self.id}>"
