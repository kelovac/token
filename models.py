from db import db
from datetime import datetime, timedelta


class TokenModel(db.Model):
    __tablename__ = 'token1'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    token = db.Column(db.String(500))
    token_expires = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow() + timedelta(minutes=30))

    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.token_expires = datetime.now() + timedelta(minutes=30)

    def get_token(self):
        return {'username': self.username,
                'token': self.token,
                'token_expires': self.token_expires}

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_token(cls, token):
        return cls.query.filter_by(token=token).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
