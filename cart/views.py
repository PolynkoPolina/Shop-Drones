import flask
from Project.config_page import config_page
from shop.models import Product, order_product
import flask_login
from .models import Order
from Project.db import DATABASE

@config_page(template_name= 'cart.html')
def render_cart():
    # 
    cart_page = 'cart'
    if flask.session['cart_page'] == 'edit_products':
        cart_page = 'edit_products'
    list_products = [] #
    cookies = flask.request.cookies.get(key= 'list_products')
    products_price = 0
    products_discount = 0
    general_products_price = 0
    if cookies:
        list_id_product = cookies.split('|')# list_id_product = ["", '1', '2', '3']
       
        for id in list_id_product:
            # 
            if id != '':
                count_id = list_id_product.count(id)
                # 
                product: Product = Product.query.get(ident= id)
                #  
                if product:
                    products_price += product.price
                    products_discount += int(product.discount)
                    general_products_price = int(products_price - products_discount)

                if [product, count_id] not in list_products:
                    # 
                    list_products.append([product, count_id]) 
        
    # 
    if (products_price != 0):
        return {
            'list_products': list_products,
            'products_price': products_price, 
            'products_discount': products_discount, 
            'general_products_price': general_products_price,
            'cart_page': cart_page
        }
    elif (products_price == 0):
        return {'list_products': list_products}

def delete_product_to_cart():
    if flask.request.method == 'POST':
        # 
        id_product = flask.request.form.get(key= "delete") # 1
        cookies = flask.request.cookies.get(key = "list_products").replace(f"|{id_product}|", '')
        # cookies = "1|1|1|2|2|2".replace("1|", "") = "2|2|2"
        response= flask.make_response(flask.redirect('/cart'))
        response.set_cookie(key= 'list_products', value= cookies)
        
        return response
        

def render_order_processing():
    # 
    if flask_login.current_user.is_authenticated:
        if flask.request.cookies.get(key= 'list_products'):
            list_products = [] #
            cookies = flask.request.cookies.get(key= 'list_products')
            flask.session['cart_page'] = 'edit_products'
            products_price = 0
            products_discount = 0
            general_products_price = 0
            if cookies:
                list_id_product = cookies.split('|')
            
                for id in list_id_product:
                    # 
                    if id != '':
                        count_id = list_id_product.count(id)
                        # 
                        product: Product = Product.query.get(ident= id)
                        #  
                        if product:
                            products_price += product.price
                            products_discount += int(product.discount)
                            general_products_price = int(products_price - products_discount)
                        if [product, count_id] not in list_products:
                            #
                            list_products.append([product, count_id]) 
        
            return flask.render_template(
                'order_processing.html', 
                list_products= list_products,
                products_price= products_price,
                products_discount= products_discount,
                general_products_price= general_products_price
                )
        else:
            return {'error': 'no_products_to_order'}
    else:
        return {'error': 'not_authenticated'}

    

def render_order_success():
    if flask_login.current_user.is_authenticated and flask.request.cookies.get(key= 'list_products'):
        list_products = [] #
        cookies = flask.request.cookies.get(key= 'list_products')
        flask.session['cart_page'] = 'edit_products'
        if cookies:
            list_id_product = cookies.split('|')
        
            for id in list_id_product:
                if id != '':
                    product: Product = Product.query.get(ident= id)
                    if product not in list_products:
                        list_products.append(product) 
        order = Order(
            user_id = flask_login.current_user.id,
            products = list_products
        )
        DATABASE.session.add(order)
        DATABASE.session.commit()
    return flask.render_template('success_order.html', order_id = order.id)
