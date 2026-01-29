import flask
import flask_login

from Project.db import DATABASE
from Project.config_page import config_page

from .apps import user

from .models import User

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

@user.route("/authorization", methods=["POST"])
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
    if flask.request.method == "POST":
        email_form = flask.request.form["email"]
        list_users = User.query.all()
        for user in list_users:
            if user.email == email_form:
                flask.render_template("restore_password.html", context={"step": ""})
    return flask.render_template("restore_password.html")