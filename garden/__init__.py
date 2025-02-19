import os
# from dotenv import load_dotenv
import secrets
from flask import Flask, render_template, redirect, url_for, session


def init_config(instance_path):
    try:
        os.makedirs(instance_path)
    except OSError:
        pass
    fp = os.path.join(instance_path, 'config.py')
    if not os.path.isfile(fp):
        with open(fp, 'w') as f:
            s_key = secrets.token_hex(16)
            s = f'SECRET_KEY="{s_key}"'
            f.write(s)


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    # app.config['TESTING'] = True

    # dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    # load_dotenv(dotenv_path)

    init_config(app.instance_path)

    app.config.from_pyfile('config.py', silent=True)
    app.config['DATABASE'] = os.path.join(app.instance_path, 'user.sqlite')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        if not 'user_id' in session:
            return redirect(url_for('auth.login'))
        # sk = app.config['SECRET_KEY']
        return render_template('index.html')

    return app

