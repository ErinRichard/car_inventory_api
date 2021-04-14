from flask_sqlalchemy import SQLAlchemy

# import uuid library from Python (universal unique identifier)
import uuid

from datetime import datetime

# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Import for Secrets Module (Provided by Python)
import secrets

# Step 2 is passing this database reference to init.py
db = SQLAlchemy()

# Step 1
# This class will create the database table for us
class User(db.Model):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default ='')
    
    # nullable = False means that it cannot be empty
    email = db.Column(db.String(150), nullable = False)
    
    # No limit on the password length. We will encrypt this
    password = db.Column(db.String, nullable = False, default = '')
    
    # Unique = True means that nothing can be duplicated within a token
    token = db.Column(db.String, default ='', unique = True)
    date_create = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email,first_name = '', last_name='', id = '', password = '', token = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)

    # Used for authentication for users to view only their cars
    def set_token(self,length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been created and added to database!'

