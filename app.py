__author__ = 'ed'
from flask import Flask, g, render_template, flash, redirect, url_for
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user
import models
import forms




DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app=Flask(__name__)
app.secret_key = 'Bacon'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Yay, you registered", "Success")
        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=forms.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POSt'))
def login():
    form= forms.LoginForm()
    if form.validate_on_submit():
        try:
            user=models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Your email or password or name dont work", 'error')
        else:
            if checked_password_hash(user.password, form.password.data):
                login_user(user)
                flash("youve been logged in", "success")
                return redirect(url_for('index'))
            else:
                flash("Your email or password or name dont work", 'error')
    return render_template('login.html', form=form)


@app.route('/')
def index():
    return 'Hey'


if __name__ == '__main__':


    app.run(debug=DEBUG, host=HOST, port=PORT)