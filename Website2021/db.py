from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import (Text)

app = Flask(__name__)
# set your mysql connection here, my local mysql is located in localhost with username & password root
# and the database named my_project
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/my_project'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(Text)
