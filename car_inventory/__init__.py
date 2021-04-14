# Import the Flask class
from flask import Flask

# Import the Config class that we created in the config.py file
from config import Config

# Import the 'site' blueprint that we created in routes.py
from .site.routes import site

from .authentication.routes import auth

from flask_migrate import Migrate
from .models import db as root_db

# Create an instance of the class
app = Flask(__name__)

app.config.from_object(Config)

# Register the application/blueprint
app.register_blueprint(site)
app.register_blueprint(auth)

root_db.init_app(app)
migrate = Migrate(app, root_db)

from car_inventory import models