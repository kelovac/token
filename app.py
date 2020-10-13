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




app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dado'
api = Api(app)
db.init_app(app)
#jwt = JWT(app, authenticate, identity)

"""
primi post request, pokupi mi username i password
salji post request u drugi app(username i password)
ako je ispravan username i password vrati True
ako je True kreiraj token i upisi u bazu username, token, token expires
vrati odgovor token
"""


@app.route('/users', methods=['POST'])
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

            token1 = TokenModel(username=data['username'],
                        token=jwt.encode({'some': 'payload'}, app.config['SECRET_KEY'], algorithm='HS256'))

            try:
                token1.save_to_db()
            except:
                return {'message': "An error occured inserting the token."}, 500


            return jsonify({'token': token.decode(UTF-8)})


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
