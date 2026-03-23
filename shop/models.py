from Project.db import DATABASE

order_product = DATABASE.Table(
    'order_product',
    DATABASE.Column('order_id', DATABASE.Integer, DATABASE.ForeignKey('order.id')),
    DATABASE.Column('product_id', DATABASE.Integer, DATABASE.ForeignKey('product.id'))
)

class Product(DATABASE.Model): 
    __tablename__ = 'product'


    id = DATABASE.Column(DATABASE.Integer, primary_key= True)
    
    product_name = DATABASE.Column(DATABASE.String(50), nullable= False)
    price = DATABASE.Column(DATABASE.Integer, nullable= False)
    discount = DATABASE.Column(DATABASE.Float, nullable= False)
    count = DATABASE.Column(DATABASE.Float, nullable= False)
    description = DATABASE.Column(DATABASE.String(450), nullable= False)
    type_product = DATABASE.Column(DATABASE.String(50), default= 'type')
    orders = DATABASE.relationship( 'Order', secondary= order_product, back_populates= 'products')


