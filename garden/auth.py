from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

from garden.db import get_db

bp = Blueprint('auth', __name__)

class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        if user is None:
            error = 'Incorrect username!'
        elif not check_password_hash(pwhash=user['password'], password=password):
            error = 'Incorrect password!'
        else:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('login.html', form=form)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))