import flask
import flask_login

from Project.db import DATABASE
from Project.config_page import config_page

from .apps import user

user.secret_key = "secret"
from .models import User, Address

@config_page(template_name= 'registration.html')
def render_registration() -> dict:
    message = ''
    if flask.request.method == "POST":
        password = flask.request.form["password"]
        confirm_password = flask.request.form["confirm_password"]
        email_form = flask.request.form["email"]

        email_model = User.query.filter_by(email = email_form).first()
        
        if email_model is None:
            if password == confirm_password:
                user = User(
                    username = flask.request.form["username"],
                    email = email_form,
                    password = password
                )
                DATABASE.session.add(user)
                DATABASE.session.commit()
                message = "successful registration"
            else:
                message = "Паролі не співпадають"
        else:
            message = "Користувач з таким email вже існує"
    
    return {'message': message}


def render_authorization():
    if flask.request.method == "POST":
        email_form = flask.request.form["email"]
        password_form = flask.request.form["password"]

        list_users = User.query.all()
        for user in list_users:
            if user.email == email_form and user.password == password_form:
                flask_login.login_user(user)
    if not flask_login.current_user.is_authenticated:
        return flask.render_template("authorization.html")
    else:
        return flask.render_template("authorization.html", context={"is_authenticated": True})
    

def logout():
    flask.session.clear()
    return flask.redirect("/")    


def render_restore_password():

    if 'step' not in flask.session:
        flask.session['step'] = 1
    if flask.request.method == "POST":
        if flask.session['step']  == 1:
            email_form = flask.request.form["email"]
            user = User.query.filter_by(email = email_form).first()
            if user:
                flask.session['email'] = email_form
                flask.session['step']  = 2

        elif flask.session['step']  == 2:
            password_form = flask.request.form['password']
            conf_password_form = flask.request.form['confirm_password']
            if password_form == conf_password_form:
                user = User.query.filter_by(email = flask.session['email']).first()
                user.password = password_form
                DATABASE.session.commit()
                flask.session['step'] = 3 
                 
    return flask.render_template('restore_password.html', step=flask.session['step'])


def render_account():
    if flask_login.current_user.is_authenticated:
        if flask.request.method == "POST":
            city_form = flask.request.form['city']
            street_form = flask.request.form['street']
            house_form = flask.request.form['house']
            appartment_form = flask.request.form['appartment']
            entrance_form = flask.request.form['entrance']

            new_address = Address(
                    city = city_form,
                    street = street_form,
                    house = house_form,
                    appartment = appartment_form,
                    entrance = entrance_form,
                    user_id = flask_login.current_user.id
                )
            DATABASE.session.add(new_address)
            DATABASE.session.commit()
            return flask.redirect('/account?page=delivery_address')
        list_address = Address.query.filter_by(user_id = flask_login.current_user.id)
        page = flask.request.args.get('page')
        return flask.render_template(f'{page}.html', context={'list_address': list_address})
    else:
        return {"error":"is_not_authenticated"}