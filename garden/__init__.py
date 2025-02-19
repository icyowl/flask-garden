import os
# from dotenv import load_dotenv
import secrets
from flask import Flask, render_template, redirect, url_for, session

def create_app():

    app = Flask(__name__)
    # app.config['TESTING'] = True

    # dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    # load_dotenv(dotenv_path)


    app.config['SECRET_KEY'] = secrets.token_hex()

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config['DATABASE'] = os.path.join(app.instance_path, 'user.sqlite')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        if not 'user_id' in session:
            return redirect(url_for('auth.login'))
        sk = app.config['SECRET_KEY']
        return render_template('index.html', sk=sk)

    return app

