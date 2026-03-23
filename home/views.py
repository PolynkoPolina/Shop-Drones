import flask
import flask_login
from os.path import abspath, join

from Project.config_page import config_page
from shop.models import Product


@config_page(template_name= 'home.html')
def render_home():
    flask.session['cart_page'] = 'cart'
    list_products = Product.query.limit(4).all()
    return {
        'list_products': list_products
    }
    


def render_about_us():
    flask.session['cart_page'] = 'cart'
    return flask.render_template('about_us.html')

def render_contacts():
    flask.session['cart_page'] = 'cart'
    return flask.render_template('contact.html')