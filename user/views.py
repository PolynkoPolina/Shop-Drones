import flask
import flask_login

from Project.db import DATABASE
from Project.config_page import config_page
from datetime import datetime

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
        page = flask.request.args.get('page')
        if flask.request.method == "POST":
            if page == 'contacts_data':

                username_form = flask.request.form['username']
                lastname_form = flask.request.form['lastname']
                middlename_form = flask.request.form['middlename']
                phone_form = flask.request.form['phone']
                bd_form = flask.request.form['dateofbirth']
                email_form = flask.request.form["email"]

                user = flask_login.current_user
                
                if user:
                    user.username = username_form
                    user.lastname = lastname_form
                    user.middlename= middlename_form
                    user.phone = phone_form
                    user.date_of_birth = datetime.strptime(bd_form, "%Y-%m-%d").date()
                    user.email = email_form

                    DATABASE.session.commit()
            elif page == "delivery_address":

                address_id = flask.request.form.get("address_id")

                city_form = flask.request.form['city']
                street_form = flask.request.form['street']
                house_form = flask.request.form['house']
                appartment_form = flask.request.form['appartment']
                entrance_form = flask.request.form['entrance']

                if address_id:
                    address = Address.query.filter_by(id=address_id, user_id=flask_login.current_user.id ).first()

                    address.city = city_form
                    address.street = street_form
                    address.house = house_form
                    address.appartment = appartment_form
                    address.entrance = entrance_form
                else:
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
        list_address = Address.query.filter_by(user_id= flask_login.current_user.id).all()
        return flask.render_template(f'{page}.html', list_address= list_address)
    else:
        return {"error":"is_not_authenticated"}