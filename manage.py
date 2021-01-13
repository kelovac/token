import os
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import app
from db import db

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
server = Server(host="127.0.0.1", port=5001)

if __name__ == '__main__':
    manager.run()
