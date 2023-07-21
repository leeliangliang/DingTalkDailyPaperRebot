from app.context import flaskApp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flaskApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
sqliteDB = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, sqliteDB)
