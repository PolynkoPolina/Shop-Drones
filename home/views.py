import flask
import flask_login
from os.path import abspath, join

from Project.config_page import config_page
from shop.models import Product


@config_page(template_name= 'home.html')
def render_home():
    model_list_products = Product.query.all()
    list_products = []
    for i in range(3):
        product = model_list_products[i]
        list_products.append(product)
    print(list_products)
    return {
        'list_product': model_list_products
    }

    