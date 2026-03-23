from Project.db import DATABASE
from shop.models import order_product


class Order(DATABASE.Model):
    __tablename__ = 'order'


    id = DATABASE.Column(DATABASE.Integer, primary_key= True)
    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('user.id'),  nullable= False)

    products = DATABASE.relationship( 'Product', secondary= order_product, back_populates='orders')
    
