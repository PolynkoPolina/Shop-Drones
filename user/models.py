from Project.db import DATABASE
from flask_login import UserMixin


class User(DATABASE.Model, UserMixin):
    __tablename__ = 'user'
    
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    
    username = DATABASE.Column(DATABASE.String(50), nullable = False)
    email = DATABASE.Column(DATABASE.String(50), nullable = False)
    password = DATABASE.Column(DATABASE.String(25), nullable = False)
    addresses = DATABASE.relationship('Address', backref= 'user', lazy= 'dynamic')

    is_admin = DATABASE.Column(DATABASE.Boolean, default = False)
    

class Address(DATABASE.Model):
        
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)

    city = DATABASE.Column(DATABASE.String(60), nullable = False)
    street = DATABASE.Column(DATABASE.String(60), nullable = False)
    house = DATABASE.Column(DATABASE.Integer, nullable = False)
    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('user.id'),  nullable = False)

    appartment = DATABASE.Column(DATABASE.Integer, nullable = True)
    entrance= DATABASE.Column(DATABASE.Integer, nullable = True)
