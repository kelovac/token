from werkzeug.security import generate_password_hash, check_password_hash
from models import Token

def authenticate(username, password):
    user = Token.find_by_username(username)
    if user and check_password_hash(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return Token.find_by_id(id)
