from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aire.db'
db = SQLAlchemy(app)

from AIRE import models  # noqa
from AIRE import routes  # noqa
