from apps.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
