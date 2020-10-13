from db import db
from datetime import datetime

class TokenModel(db.Model):
    __tablename__ = 'token'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    token = db.Column(db.String(80))
    #token_expires = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())

    def __init__(self, username, token):
        self.username = username
        self.token = token

    def get_token(self):
        return {'username': self.username,
                'token': self.token,
                'token_expires': self.token_expires()}

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
