from werkzeug.security import generate_password_hash, check_password_hash
from models import TokenModel


def authenticate(username, password):
    user = TokenModel.find_by_username(username)
    if user and check_password_hash(user.password, password):
        return user


def identity(payload):
    token = payload['identity']
    return TokenModel.find_by_token(token)
