import requests
from db import db
from flask_restful import Api
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import TokenModel
#from security import authenticate, identity
import jwt
from datetime import datetime
import os
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)




app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'dado'
api = Api(app)
db.init_app(app)
jwt = JWTManager(app)

"""
primi post request, pokupi mi username i password
salji post request u drugi app(username i password)
ako je ispravan username i password vrati True
ako je True kreiraj token i upisi u bazu username, token, token expires
vrati odgovor token
"""


@app.route('/token', methods=['POST'])
def get_user():
    if request.method == 'POST':

        data = request.get_json()

        username = data['username']
        password = data['password']

        payload = {
        "username": username,
        "password": password}

        response = requests.post('http://127.0.0.1:5000/login', json=payload)

        if response.status_code == 200:

            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200

            try:
                access_token.save_to_db()
            except:
                return {'message': "An error occured inserting the token."}, 500





        else:
            return response.json(), 400

    return "ss"




def check_token():
    """
    iz druge app mi stize token
    radim proveru u bazi da li token postoji
    ako postoji odg sa True, ako ne sa False
    """


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
